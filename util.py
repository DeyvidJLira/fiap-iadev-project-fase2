import math
from typing import List, Tuple
from attraction import Attraction

def calculate_distance(p_from: Tuple[float, float], p_target: Tuple[float, float]):
    R = 6371 
    dlat = math.radians(p_target[0] - p_from[0])
    dlon = math.radians(p_target[1] - p_from[1])
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(p_from[0])) * math.cos(math.radians(p_target[1])) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c 


def geolocation_to_pixel(lat, lon, lat_min, lat_max, lon_min, lon_max, width, height):
    x = (lon - lon_min) / (lon_max - lon_min) * width + width/2 # (width/2) é um modificador para posicionar em uma área desejada da cena
    y = (lat_max - lat) / (lat_max - lat_min) * height + height/2.5 # (height/2.5)  é um modificador para posicionar em uma área desejada da cena
    return int(abs(x)), int(abs(y))
    

def calculate_total_distance(roadmap: List[Attraction]) -> float:
    total_distance = sum(
        calculate_distance(
            roadmap[i].location, roadmap[i+1].location
        ) for i in range(len(roadmap) - 1)
    )
    return total_distance


def calculate_total_cost(roadmap: List[Attraction]) -> float:
    total_cost = sum(
       it.cost for it in roadmap
    )
    return total_cost


