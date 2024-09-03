from attraction import Attraction

WIDTH_SCREEN, HEIGHT_SCREEN = 1280, 720
WIDTH_MAP, HEIGHT_MAP = WIDTH_SCREEN /2, HEIGHT_SCREEN/2
FPS = 60
POINT_COLOR = "black"
TEXT_COLOR = "black"
PATH_COLOR = (128, 128, 128)
PATH_BEST_SOLUTION = (255, 0, 0)

N_GENERATIONS = 50
POPULATION_SIZE = 50
MUTATION_PROBABILITY = 0.2

LAT_MIN, LAT_MAX = -29.3500, -29.4200
LON_MIN, LON_MAX = -50.8700, -50.9100

ATTRACTIONS = [
    Attraction("Mini Mundo", "./images/mini_mundo.jpg", 53, 2, [-29.3876033,-50.8704896]),
    Attraction("Lago Negro", "./images/lago_negro.jpg", 30, 3, [-29.4177228,-50.8957769]),
    Attraction("Jardim do Amor", "./images/jardim_amor.jpg", 25, 3, [-29.3857825,-50.8866468]),
    Attraction("Aldeia do Papai Nodel", "./images/aldeia_papai_noel.jpg", 50, 2, [-29.4032139,-50.8790896]),
    Attraction("Snowland", "./images/snowland.jpg", 199.9, 5, [-29.3953631,-50.9058695]),
    Attraction("Praça das Etnias", "./images/praca_etnias.jpg", 50, 0.5, [-29.3801653,-50.8761832]),
    Attraction("Café Colonial Bela Vista", "./images/cafe_colonial.jpg", 150, 1.5, [-29.3801653,-50.8761832]),
    Attraction("Casa da Velha Bruxa", "./images/casa_velha_bruxa.jpg", 150, 1.5, [-29.3601653,-50.8761832])
]
