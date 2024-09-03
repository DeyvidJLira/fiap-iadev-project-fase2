from enum import Enum
from attraction import Attraction
from typing import List
from util import calculate_total_distance, calculate_total_cost
import random

def calculate_fitness(roadmap: List[Attraction]):
    return calculate_total_distance(roadmap)


def create_roadmap(attractions) -> List[Attraction]:
    attractions_cp = attractions[:]
    roadmap = []
    while len(attractions_cp) > 0:
        attraction = random.choice(attractions_cp)
        attractions_cp.remove(attraction)
        roadmap.append(attraction)
    return roadmap

# def create_roadmap(attractions, budget_max) -> List[Attraction]:
#     attractions_cp = attractions[:]
#     roadmap = []
#     budget = 0
#     while budget < budget_max * 0.9 and len(attractions_cp) > 0:
#         attraction = random.choice(attractions_cp)
#         attractions_cp.remove(attraction)
#         if budget + attraction.cost <= budget_max:
#             roadmap.append(attraction)
#             budget += attraction.cost
#     return roadmap

def crossover(roadmap1: List[Attraction], roadmap2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    parent1_lenght = len(roadmap1)
    parent2_lenght = len(roadmap2)

    start_index = random.randint(0, parent1_lenght -1)
    end_index = random.randint(start_index + 1, parent1_lenght)

    roadmap_child1 = roadmap1[start_index:end_index]
    roadmap_child2 = roadmap2[start_index:end_index]

    remaining_positions = [i for i in range(parent1_lenght) if i < start_index or i >= end_index]
    remaining_genes = [ gene for gene in roadmap2 if gene not in roadmap_child1]

    for position, gene in zip(remaining_positions, remaining_genes):
        roadmap_child1.insert(position, gene)

    remaining_positions = [i for i in range(parent2_lenght) if i < start_index or i >= end_index]
    remaining_genes = [ gene for gene in roadmap1 if gene not in roadmap_child2]

    for position, gene in zip(remaining_positions, remaining_genes):
        roadmap_child2.insert(position, gene)
    
    return roadmap_child1, roadmap_child2


class MutateMethod(Enum):
    SWAP = 1
    INVERSION = 2
    INSERTION = 3
    SHUFFLE = 4

def mutate(method: MutateMethod, roadmap: List[Attraction], mutation_probability: float) -> List[Attraction]:
    mutated_solution = roadmap[:]

    if random.random() < mutation_probability:
        if len(roadmap) < 2:
            return roadmap

        index = random.randint(0, len(roadmap) - 2)

        mutated_solution[index], mutated_solution[index + 1] = roadmap[index + 1], roadmap[index]

    return mutated_solution

