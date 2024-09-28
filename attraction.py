# Representação do modelo
class Attraction:
    def __init__(self, name: str, image_path: str,  cost: int, score: float, location: tuple[float, float]):
        self.name = name
        self.image_path = image_path
        self.cost = cost
        self.score = score
        self.location = location

    def __repr__(self):
        return f'Attraction({self.name})'

    def __eq__(self, other):
        if isinstance(other, Attraction):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)