from attraction import Attraction
from genetic_algorithm import CrossoverMethod, MutateMethod

MAP_BASE_LOCATION = [-29.3863118,-50.881217] # Geolocalização base para renderização do mapa
ZOOM_START = 14.5 # Zoom inicial do mapa

N_GENERATIONS = 150 # Total de gerações
POPULATION_SIZE = 5 # Tamanho da população
CROSSOVER_METHOD = CrossoverMethod.OX2 # Método de cruzamento à ser utilizado pela aplicação
MUTATION_METHOD = MutateMethod.SHUFFLE # Método de mutação à ser utilizado pela aplicação
MUTATION_PROBABILITY = 0.1 # Probabilidade da mutação ocorrer durando a execução da aplicação

ATTRACTIONS = [
    Attraction("Mini Mundo", "/static/images/mini_mundo.jpg", 53, 4.5, [-29.385693,-50.8787115]),
    Attraction("Lago Negro", "/static/images/lago_negro.jpg", 30, 4, [-29.3947609,-50.874736]),
    Attraction("Jardim do Amor", "/static/images/jardim_amor.jpg", 15, 3, [-29.3831317,-50.8852863]),
    Attraction("Aldeia do Papai Noel", "/static/images/aldeia_papai_noel.jpg", 25, 2, [-29.3792404,-50.8720155]),
    Attraction("Snowland", "/static/images/snowland.jpg", 59.9, 4.4, [-29.3953631,-50.9058695]),
    Attraction("Praça das Etnias", "/static/images/praca_etnias.jpg", 25, 1.5, [-29.3801653,-50.8761832]),
    Attraction("Café Colonial Bela Vista", "/static/images/cafe_colonial.jpg", 150, 3.5, [-29.3801653,-50.8761832]),
    Attraction("Casa da Velha Bruxa", "/static/images/casa_velha_bruxa.jpg", 90, 2.5, [-29.3783341,-50.8743209]),
    Attraction("Florybal Chocolates", "/static/images/florybal.jpg", 79.9, 3.0, [-29.3827156,-50.8831821]),
    Attraction("Praça Major Nicoletti", "/static/images/praça_major_nicoletti.jpg", 25, 1.5, [-29.3800249,-50.8735688]),
    Attraction("Hector Pizzaria", "/static/images/hector_pizzaria.jpg", 199.9, 5.0, [-29.3858376,-50.8742598]),
    Attraction("Ecoparque Sperry", "/static/images/ecoparque.png", 45, 4.8, [-29.3889295,-50.8562059]),
    Attraction("Hollywood Dream Cars", "/static/images/hollywood_dream_cars.jpg", 99, 2.2, [-29.3646887,-50.8611681])
]

BUDGET_MAX = 200 # Orçamento máximo do intineário resultante
