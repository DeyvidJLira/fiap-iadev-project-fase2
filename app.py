from setup import *
from draw_functions import draw_attractions, draw_paths, draw_plot, draw_text
from util import calculate_total_distance, calculate_total_cost
from enum import Enum
from genetic_algorithm import MutateMethod, create_roadmap, calculate_fitness, crossover, mutate

import pygame
import sys
import random
import itertools

BACKGROUND = pygame.transform.scale(pygame.image.load("./images/background.jpg"), (WIDTH_SCREEN, HEIGHT_SCREEN))

class State(Enum):
    IN_ALG = 1
    IN_ALG_FINISHED = 2
    IN_REPORT = 3

class App():
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init() 
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption("Best RoadMap")
        self.clock = pygame.time.Clock()
        self.running = True 
        self.state = State.IN_ALG
        self.generation_counter = itertools.count(start=1)       
        self.generation = 0
        self.population = [create_roadmap(ATTRACTIONS) for _ in range(POPULATION_SIZE)] 
        self.best_fitness_values = []
        self.best_solutions = []
        # end init


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.state == State.IN_ALG_FINISHED:
                        self.state = State.IN_REPORT
                    if event.key == pygame.K_x and self.state == State.IN_REPORT:
                        self.running = False

            if self.state == State.IN_ALG:
                self.scene_in_alg()
            elif self.state == State.IN_ALG_FINISHED:
                self.scene_in_alg_finished()
            elif self.state == State.IN_REPORT:
                self.scene_in_report()

        pygame.quit()
        sys.exit()
        # end run
            

    def scene_in_alg(self):
        self.screen.blit(BACKGROUND, (0, 0))

        draw_text(self.screen, "Processando...", (540, 60))

        draw_attractions(self.screen)

        self.population.sort(key=lambda it: calculate_fitness(it), reverse=False)

        new_population = [self.population[0]]

        self.best_fitness = calculate_fitness(self.population[0])
        self.best_solution = self.population[0]

        self.best_fitness_values.append(self.best_fitness)
        self.best_solutions.append(self.best_solution)

        if(self.generation >= N_GENERATIONS):
            self.state = State.IN_ALG_FINISHED
            return
        else:
            self.generation = next(self.generation_counter)

        draw_plot(self.screen, list(range(len(self.best_fitness_values))),
              self.best_fitness_values, y_label="Fitness - Distance (KMs)")

        draw_paths(self.screen, path=[it.location for it in self.best_solution], rgb_color=PATH_BEST_SOLUTION, width=3)
        draw_paths(self.screen, path=[it.location for it in self.population[1]], rgb_color=PATH_COLOR, width=3)
        
        print(f"Generation {self.generation} Total Distance the best {calculate_total_distance(self.best_solution):.2f}km and Total cost: R$ {calculate_total_cost(self.best_solution):.2f}")

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.choices(self.population[:10], k=2)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(MutateMethod.SWAP, child1, MUTATION_PROBABILITY)
            child2 = mutate(MutateMethod.SWAP, child2, MUTATION_PROBABILITY)

            new_population.append(child1)
            new_population.append(child2)

        self.population = new_population

        pygame.display.flip()

        self.clock.tick(FPS)

        # end scene alg   
    

    def scene_in_alg_finished(self):
        self.screen.blit(BACKGROUND, (0, 0))

        draw_attractions(self.screen)     
        draw_plot(self.screen, list(range(len(self.best_fitness_values))), self.best_fitness_values, y_label="Fitness - Distance (KMs)")
        draw_paths(self.screen, [it.location for it in self.best_solutions[0]], rgb_color=PATH_BEST_SOLUTION, width=3)    
        draw_text(self.screen, "Press 'enter' to show report", (500, 60))

        pygame.display.flip()
        self.clock.tick(FPS)
        # end scene in alg finished


    def scene_in_report(self):
        self.screen.blit(BACKGROUND, (0, 0))

        draw_text(self.screen, "Report (Press 'x' to exit)", (300, 90))

        y = 150

        best_roadmap = self.population[0]
        for index, attraction in enumerate(best_roadmap):
            draw_text(self.screen, f"{attraction.name}: Custo R${attraction.cost}, Tempo {attraction.time}", (300, y + (index * 25)))
            
        pygame.display.flip()
        self.clock.tick(FPS)
    # end scene in report