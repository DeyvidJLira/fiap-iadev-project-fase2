import math
from typing import List, Tuple
from attraction import Attraction

# Calcula a distância entre dois pontos cartesianos
def calculate_distance(p_from: Tuple[float, float], p_target: Tuple[float, float]):
    R = 6371 
    dlat = math.radians(p_target[0] - p_from[0])
    dlon = math.radians(p_target[1] - p_from[1])
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(p_from[0])) * math.cos(math.radians(p_target[1])) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c 

# Calcula a distância total que seria pecorrida naquele roteiro, eventos que estejam dentro do orçamento, considerando uma reta entre dois pontos cartesianos 
def calculate_total_distance_limited(roadmap: List[Attraction], budget_max: float) -> float:
    total_events = calculate_total_events_until_budget(roadmap, budget_max)
    
    total_distance = sum(
        calculate_distance(
            roadmap[i].location, roadmap[i+1].location
        ) for i in range(len(roadmap[:total_events]) - 1)
    )
    return total_distance

# Calcula a total dos eventos de um roteiro que estejam dentro do orçamento
def calculate_total_events_until_budget(roadmap: List[Attraction], budget_max: float) -> int:
    budget = 0
    total_events = 0

    for attraction in roadmap:
        if(budget + attraction.cost > budget_max):
            break
        else:
            budget += attraction.cost
            total_events += 1

    return total_events

# Calcula o custo total dos eventos de um roteiro que estejam dentro do orçamento
def calculate_total_cost_limited(roadmap: List[Attraction], budget_max: float) -> float:
    total_events = calculate_total_events_until_budget(roadmap, budget_max)

    total_cost = sum(
       it.cost for it in roadmap[:total_events]
    )
    return total_cost

# Calcula a pontuação total dos eventos de um roteiro que estejam dentro do orçamento
def calculate_total_score_limited(roadmap: List[Attraction], budget_max: float) -> float:
    total_events = calculate_total_events_until_budget(roadmap, budget_max)

    total_score = sum(
       it.score for it in roadmap[:total_events]
    )
    return total_score
