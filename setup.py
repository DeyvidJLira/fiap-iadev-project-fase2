from attraction import Attraction
from genetic_algorithm import CrossoverMethod, MutateMethod

MAP_BASE_LOCATION = [-29.3801653,-50.8761832] # Geolocalização base para renderização do mapa

N_GENERATIONS = 150 # Total de gerações
POPULATION_SIZE = 3 # Tamanho da população
CROSSOVER_METHOD = CrossoverMethod.OX2 # Método de cruzamento à ser utilizado pela aplicação
MUTATION_METHOD = MutateMethod.SWAP # Método de mutação à ser utilizado pela aplicação
MUTATION_PROBABILITY = 0.1 # Probabilidade da mutação ocorrer durando a execução da aplicação

ATTRACTIONS = [
    Attraction("Mini Mundo", "/static/images/mini_mundo.jpg", 53, 4.5, [-29.3876033,-50.8704896]),
    Attraction("Lago Negro", "/static/images/lago_negro.jpg", 30, 3.5, [-29.4177228,-50.8957769]),
    Attraction("Jardim do Amor", "/static/images/jardim_amor.jpg", 25, 3, [-29.3857825,-50.8866468]),
    Attraction("Aldeia do Papai Nodel", "/static/images/aldeia_papai_noel.jpg", 50, 1, [-29.4032139,-50.8790896]),
    Attraction("Snowland", "/static/images/snowland.jpg", 59.9, 4, [-29.3953631,-50.9058695]),
    Attraction("Praça das Etnias", "/static/images/praca_etnias.jpg", 50, 1.5, [-29.3801653,-50.8761832]),
    Attraction("Café Colonial Bela Vista", "/static/images/cafe_colonial.jpg", 150, 3, [-29.3801653,-50.8761832]),
    Attraction("Casa da Velha Bruxa", "/static/images/casa_velha_bruxa.jpg", 120, 2.5, [-29.3601653,-50.8761832])
]

BUDGET_MAX = 200 # Orçamento máximo do intineário resultante
