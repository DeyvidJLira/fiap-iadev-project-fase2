# Representação do modelo
class Attraction:
    def __init__(self, name: str, image_path: str,  cost: int, score: float, location: tuple[float, float]):
        self.name = name
        self.image_path = image_path
        self.cost = cost
        self.score = score
        self.location = location
