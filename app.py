from setup import *
from draw_functions import draw_attractions, draw_plot
from util import calculate_total_distance_limited, calculate_total_events_until_budget, calculate_total_cost_limited, calculate_total_score_limited
from genetic_algorithm import create_roadmap, calculate_fitness, crossover, mutate

from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio

import folium
import folium.map
import random

class GeneticVars:
    def __init__(self):
        self.generation = 0
        self.population = [create_roadmap(ATTRACTIONS) for _ in range(POPULATION_SIZE)] 
        self.best_fitness_values = []
        self.best_solutions = []


app = FastAPI(
    title = "Guia Turístico Genético",
    description = """
Guia Turístico Genético API é uma aplicação destinada a encontrar o melhor roteiro.

## Dependências:
- FastAPI (https://fastapi.tiangolo.com/)
- Folium (https://python-visualization.github.io/folium/latest/)
- Uvicorn (https://www.uvicorn.org/)
""",
    version = "0.2.0",
    license_info = {
        "name": "MIT"
    }
) 
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.state.path_data = []
app.state.genetic_vars = GeneticVars()


# Função destinada a criar o mapa, incluir as atrações e retornar em HTML
def create_map():
    app.state.map = folium.Map(
        MAP_BASE_LOCATION, 
        zoom_start=13.3, 
        tiles="cartodb positron",
        scrollWheelZoom=False,
        dragging=False,        
        zoomControl=False,
        keyboard=False,        
        touchZoom=False,    
        attributionControl=False
    )
    draw_attractions(app.state.map)

    return app.state.map._repr_html_()


# Função destinada a execução do algoritmo genético objetivando alcançar a melhor solução
async def execute_genetic_algorithm():
    for app.state.genetic_vars.generation in range(N_GENERATIONS):
        await asyncio.sleep(0.2)
        app.state.path_data.clear()

        app.state.genetic_vars.population.sort(key=lambda it: calculate_fitness(it, BUDGET_MAX), reverse=False)

        new_population = [app.state.genetic_vars.population[0]]

        best_fitness = calculate_fitness(app.state.genetic_vars.population[0], BUDGET_MAX)
        best_solution = app.state.genetic_vars.population[0]

        app.state.genetic_vars.best_fitness_values.append(best_fitness)
        app.state.genetic_vars.best_solutions.append(best_solution)

        limit = calculate_total_events_until_budget(best_solution, BUDGET_MAX)
        app.state.path_data.append(list(it.location) for it in best_solution[:limit])

        yield app.state.path_data

        app.state.genetic_vars.generation += 1

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.choices(app.state.genetic_vars.population[:10], k=2)

            child1, child2 = crossover(CROSSOVER_METHOD, parent1, parent2)

            child1 = mutate(MUTATION_METHOD, child1, MUTATION_PROBABILITY)
            child2 = mutate(MUTATION_METHOD, child2, MUTATION_PROBABILITY)

            new_population.append(child1)
            new_population.append(child2)

        app.state.genetic_vars.population = new_population
            

@app.get('/', description="""
Rota destinada a inicialização e retornar página contendo o mapa.
""")
def index(request: Request):
    app.state.path_data = []
    app.state.genetic_vars = GeneticVars()
    
    map_html = create_map()
    return templates.TemplateResponse('map.html', {"request": request, "map_html": map_html})


@app.get("/plot", description="""
Rota destinada a gerar o gráfico de geração x fitness e retornar como imagem png.
""")
async def get_plot():
    buf = draw_plot(list(range(len(app.state.genetic_vars.best_fitness_values))), app.state.genetic_vars.best_fitness_values, y_label="Fitness")
    return StreamingResponse(buf, media_type="image/png")


@app.get("/report", response_class=HTMLResponse, description="""
Rota destinada a gerar o relatório da melhor solução e retornar em texto com sintaxe HTML.
""")
def get_report():
    best_roadmap = app.state.genetic_vars.best_solutions[len(app.state.genetic_vars.best_solutions) - 1]
    total_events = calculate_total_events_until_budget(best_roadmap, BUDGET_MAX)

    report = "<table><th>Ordem</th><th>Evento</th><th>Custo</th><th>Avaliação</th>"
    
    for index, attraction in enumerate(best_roadmap[:total_events]):
        report += f"<tr><td>{index + 1}</td><td>{attraction.name}</td><td>R${attraction.cost}</td><td>{attraction.score}</td></tr>"
    
    report += "</table>"

    report += f"<br><b>Total Distance:</b> {calculate_total_distance_limited(best_roadmap, BUDGET_MAX):.2f}km<br><b>Total Cost:</b> R$ {calculate_total_cost_limited(best_roadmap, BUDGET_MAX):.2f}<br><b>Total score:</b> {calculate_total_score_limited(best_roadmap, BUDGET_MAX):.0f}"
    return report


# Websocket destinado a cada geração compartilhar o path da melhor solução encontrada
@app.websocket('/ws')
async def update(websocket: WebSocket):
    await websocket.accept()
    async for generation_data in execute_genetic_algorithm():
        generation_data_list = [list(item) for item in generation_data]
        await websocket.send_json({"path": generation_data_list})
    await websocket.close()