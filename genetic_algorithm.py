from enum import Enum
from attraction import Attraction
from typing import List
from util import calculate_total_distance_limited, calculate_total_events_until_budget, calculate_total_score_limited
import random

# Função destinada a dar uma pontuação de aptidão para uma determinada solução. No atual contexto, o mais apto sempre terá um valor menor.
def calculate_fitness(roadmap: List[Attraction], budget_max: float) -> float:
    return calculate_total_distance_limited(roadmap, budget_max) - calculate_total_events_until_budget(roadmap, budget_max) - calculate_total_score_limited(roadmap, budget_max)

#  Cria uma solução de intineário de forma aleatória.
def create_roadmap(attractions) -> List[Attraction]:
    attractions_cp = attractions[:]
    roadmap = []
    while len(attractions_cp) > 0:
        attraction = random.choice(attractions_cp)
        attractions_cp.remove(attraction)
        roadmap.append(attraction)
    return roadmap

# Enum dos métodos crossover disponíves nessa aplicação
class CrossoverMethod(Enum):
    OX1 = 1
    OX2 = 2
    CX = 3

# Chama a função de cruzamento genético indicado e retorna dois filhos
def crossover(method: CrossoverMethod, roadmap1: List[Attraction], roadmap2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    match method:
        case CrossoverMethod.OX1: return crossover_ox1(roadmap1, roadmap2)
        case CrossoverMethod.OX2: return crossover_ox2(roadmap1, roadmap2)
        case CrossoverMethod.CX: return crossover_cx(roadmap1, roadmap2)
        
        
# Ordered Crossover a partir de uma subsequência e devolve dois filhos
def crossover_ox1(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    size = len(parent1) # isso é por conta que o tamanho dos pais são sempre iguais

    start_index = random.randint(0, size -1)
    end_index = random.randint(start_index + 1, size)

    child1 = parent1[start_index:end_index]
    child2 = parent2[start_index:end_index]

    def fill_child(child, parent_origin_length, parent_target):
        remaining_positions = [i for i in range(parent_origin_length) if i < start_index or i >= end_index]
        remaining_genes = [ gene for gene in parent_target if gene not in child]    

        for position, gene in zip(remaining_positions, remaining_genes):
            child.insert(position, gene)

        return child

    child1 = fill_child(child1, size, parent2)
    child2 = fill_child(child1, size, parent1)
    
    return child1, child2

# Ordered Crossover a partir de um conjuto de posições aleatórias e devolve dois filhos
def crossover_ox2(parent1: List[Attraction], parent2: List[Attraction]) -> tuple[List[Attraction], List[Attraction]]:
    size = len(parent1)  # isso é por conta que o tamanho dos pais são sempre iguais

    child1, child2 = [None] * size, [None] * size

    n_positions = random.randint(1, size - 1)
    positions = random.sample(range(size), n_positions)

    for position in positions:
        child1[position] = parent1[position]
        child2[position] = parent2[position]
    

    def fill_child(child: List[Attraction], parent_target: List[Attraction]) :
        current_pos = 0
        for gene in parent_target:
            if gene not in child:
                while child[current_pos] is not None:
                    current_pos += 1
                child[current_pos] = gene

        return child

    child1 = fill_child(child1, parent2)
    child2 = fill_child(child1, parent1)
    
    return child1, child2


# Cycle Crossover para troca de ciclos do material genético dos pais e devolve dois filhos
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

    def fill_when_none(size: int, child: List[Attraction], parent: List[Attraction]):
        for i in range(size):
            if child[i] is None:
                child[i] = parent[i]
        return child

    child1 = fill_when_none(size, child1, parent2)
    child2 = fill_when_none(size, child2, parent1)

    return child1, child2

# Enum dos métodos de mutação disponíves nessa aplicação
class MutateMethod(Enum):
    SWAP = 1
    INVERSION = 2
    INSERTION = 3
    SHUFFLE = 4

# Chama a função de mutação indicado em cima da solução passada segundo a probabilidade de mutação
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

# Função de mutação de troca de posição de genes do material genético
def mutateSwap(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    index1 = random.randint(0, final_position_list)
    index2 = random.randint(0, final_position_list)

    while index1 == index2:
        index2 = random.randint(0, final_position_list)

    mutated_solution[index1], mutated_solution[index2] = roadmap[index2], roadmap[index1]

    return mutated_solution

# Função de mutação que realiza a inversão dos genes de uma subsequencia
def mutateInversion(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    start = random.randint(0, final_position_list - 1)
    end = random.randint(start + 1, final_position_list)

    mutated_solution[start:end+1] = mutated_solution[start:end+1][::-1]

    return mutated_solution

# Função de mutação que visa tirar um gene de uma posição e coloca-lo em outra, alterando assim a ordem
def mutateInsertion(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    index_to_remove = random.randint(0, final_position_list)
    index_to_insert = random.randint(0, final_position_list)

    gene = mutated_solution.pop(index_to_remove)

    mutated_solution.insert(index_to_insert, gene)

    return mutated_solution

# Função de mutação que visa embaralhar os genes de uma subsequência
def mutateShuffle(roadmap: List[Attraction]) -> List[Attraction]:
    mutated_solution = roadmap[:]
    final_position_list = len(roadmap) - 1

    start = random.randint(0, final_position_list - 1)
    end = random.randint(start + 1, final_position_list)

    subsequence = roadmap[start:end+1]
    random.shuffle(subsequence)

    mutated_solution[start:end+1] = subsequence

    return mutated_solution
