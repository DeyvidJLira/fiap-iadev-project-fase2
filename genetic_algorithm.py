from enum import Enum
from attraction import Attraction
from typing import List
from util import calculate_total_distance, calculate_total_events_until_budget, calculate_total_score_limited
import random

def calculate_fitness(roadmap: List[Attraction], budget_max: float) -> float:
    return calculate_total_distance(roadmap) - calculate_total_events_until_budget(roadmap, budget_max) - calculate_total_score_limited(roadmap, budget_max)


def create_roadmap(attractions) -> List[Attraction]:
    attractions_cp = attractions[:]
    roadmap = []
    while len(attractions_cp) > 0:
        attraction = random.choice(attractions_cp)
        attractions_cp.remove(attraction)
        roadmap.append(attraction)
    return roadmap

class CrossoverMethod(Enum):
    OX = 1
    PMX = 2
    CX = 3
    OX1 = 4


def crossover(method: CrossoverMethod, roadmap1: List[Attraction], roadmap2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    match method:
        case CrossoverMethod.OX: return crossover_ox(roadmap1, roadmap2)
        case CrossoverMethod.PMX: return crossover_pmx(roadmap1, roadmap2)
        case CrossoverMethod.CX: return crossover_cx(roadmap1, roadmap2)
        case CrossoverMethod.OX1: return crossover_ox1(roadmap1, roadmap2)
        
# Order Crossover
def crossover_ox(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    size = len(parent1)

    index1, index2 = sorted(random.sample(range(size), 2))

    child1 = parent1[index1:index2]
    child2 = parent2[index1:index2]

    current_pos = index2
    for gene in parent2:
        if gene not in child1:
            if current_pos >= size:
                current_pos = 0
            child1.insert(current_pos, gene)
            current_pos += 1

    current_pos = index2
    for gene in parent1:
        if gene not in child2:
            if current_pos >= size:
                current_pos = 0
            child2.insert(current_pos, gene)
            current_pos += 1

    return child1, child2

# Partially Mapped Crossover
def crossover_pmx(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    size = len(parent1)
    
    index1, index2 = sorted(random.sample(range(size), 2))

    child1, child2 = [None] * size, [None] * size

    child1[index1:index2] = parent1[index1:index2]
    child2[index1:index2] = parent2[index1:index2]

    for i in range(index1, index2):
        gene = parent2[i]
        if gene not in child1:
            while child1[parent1.index(gene)] is not None:
                gene = parent2[parent1.index(gene)]
            child1[parent1.index(gene)] = parent2[i]

    for i in range(index1, index2):
        gene = parent1[i]
        if gene not in child2:
            while child2[parent2.index(gene)] is not None:
                gene = parent1[parent2.index(gene)]
            child2[parent2.index(gene)] = parent1[i]

    for i in range(size):
        if child1[i] is None:
            child1[i] = parent2[i]
        if child2[i] is None:
            child2[i] = parent1[i]

    return child1, child2

# Cycle Crossover
def crossover_cx(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    size = len(parent1)
    
    child1, child2 = [None] * size, [None] * size

    cycle = []
    index = 0    
    while index not in cycle:
        cycle.append(index)
        index = parent1.index(parent2[index])

    for i in cycle:
        child1[i] = parent1[i]
        child2[i] = parent2[i]

    for i in range(size):
        if child1[i] is None:
            child1[i] = parent2[i]
        if child2[i] is None:
            child2[i] = parent1[i]

    return child1, child2

# Ordered Crossover
def crossover_ox1(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    parent1_lenght = len(parent1)
    parent2_lenght = len(parent2)

    start_index = random.randint(0, parent1_lenght -1)
    end_index = random.randint(start_index + 1, parent1_lenght)

    child1 = parent1[start_index:end_index]
    child2 = parent2[start_index:end_index]

    remaining_positions = [i for i in range(parent1_lenght) if i < start_index or i >= end_index]
    remaining_genes = [ gene for gene in parent2 if gene not in child1]

    for position, gene in zip(remaining_positions, remaining_genes):
        child1.insert(position, gene)

    remaining_positions = [i for i in range(parent2_lenght) if i < start_index or i >= end_index]
    remaining_genes = [ gene for gene in parent1 if gene not in child2]

    for position, gene in zip(remaining_positions, remaining_genes):
        child2.insert(position, gene)
    
    return child1, child2


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
