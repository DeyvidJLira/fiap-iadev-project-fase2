from typing import List, Tuple
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from setup import *
from util import geolocation_to_pixel
import pygame

matplotlib.use("Agg")

def draw_plot(screen: pygame.Surface, x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness') -> None:
    fig, ax = plt.subplots(figsize=(4, 3), dpi=80)
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0) 
    ax.plot(x, y)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_argb()

    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "ARGB")
    screen.blit(surf, (0, HEIGHT_SCREEN - 240))


def draw_paths(screen: pygame.Surface, path: List[Tuple[float, float]], rgb_color: Tuple[int, int, int], width: int = 3):
    pygame.draw.lines(screen, rgb_color, True, path, width=width)


def draw_attractions(p_screen: pygame.Surface):
    for attraction in ATTRACTIONS:
            x, y = geolocation_to_pixel(attraction.location[0], attraction.location[1], LAT_MIN, LAT_MAX, LON_MIN, LON_MAX, WIDTH_MAP, HEIGHT_MAP)
            attraction.draw(p_screen, x, y)


def draw_text(screen: pygame.Surface, text: str, position: tuple[int, int]) -> None:
    font_size = 24
    my_font = pygame.font.SysFont('Arial', font_size)
    text_surface = my_font.render(text, False, TEXT_COLOR)
    
    screen.blit(text_surface, position)