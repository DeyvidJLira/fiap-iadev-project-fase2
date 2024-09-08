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
    if random.random() < mutation_probability:
        if len(roadmap) < 2:
            return roadmap
        
        match method:
            case MutateMethod.SWAP: return mutateSwap(roadmap)
            case MutateMethod.INVERSION: return mutateInversion(roadmap)
            case MutateMethod.INSERTION: return mutateInsertion(roadmap)
            case MutateMethod.SHUFFLE: return mutateShuffle(roadmap)
            
    return roadmap


def mutateSwap(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    index1 = random.randint(0, final_position_list)
    index2 = random.randint(0, final_position_list)

    while index1 == index2:
        index2 = random.randint(0, final_position_list)

    mutated_solution[index1], mutated_solution[index2] = roadmap[index2], roadmap[index1]

    return mutated_solution


def mutateInversion(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    start = random.randint(0, final_position_list - 1)
    end = random.randint(start + 1, final_position_list)

    mutated_solution[start:end+1] = mutated_solution[start:end+1][::-1]

    return mutated_solution


def mutateInsertion(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    index_to_remove = random.randint(0, final_position_list)
    index_to_insert = random.randint(0, final_position_list)

    gene = mutated_solution.pop(index_to_remove)

    mutated_solution.insert(index_to_insert, gene)

    return mutated_solution


def mutateShuffle(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    start = random.randint(0, final_position_list - 1)
    end = random.randint(start + 1, final_position_list)

    subsequence = roadmap[start:end+1]
    random.shuffle(subsequence)

    mutated_solution[start:end+1] = subsequence

    return mutated_solution
