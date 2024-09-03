from typing import Tuple
import pygame

class Attraction:
    def __init__(self, name: str, image_path: str,  cost: int, time: float, location: Tuple[float, float]):
        self.name = name
        self.cost = cost
        self.time = time
        self.location = location
        self.image = pygame.image.load(image_path)


    def draw(self, screen: pygame.Surface, x: int, y: int):
        screen.blit(self.get_image_resized(), (x, y))

    
    def get_image_resized(self) -> pygame.Surface:
        return pygame.transform.scale(self.image, (64, 64))
    
