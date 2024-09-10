from typing import List, Tuple
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from setup import *
from util import geolocation_to_pixel
import pygame
import copy

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
    path_cp = copy.deepcopy(path)
    for element in path_cp:
         element[0], element[1] = geolocation_to_pixel(element[0], element[1], LAT_MIN, LAT_MAX, LON_MIN, LON_MAX, WIDTH_MAP, HEIGHT_MAP)

    pygame.draw.lines(screen, rgb_color, False, path_cp, width=width)
    for i, target in enumerate(path_cp):
        draw_text(screen, str(i + 1), [target[0], target[1] - 64], TEXT_PATH_POINT)


def draw_attractions(p_screen: pygame.Surface):
    for attraction in ATTRACTIONS:
        x, y = geolocation_to_pixel(attraction.location[0], attraction.location[1], LAT_MIN, LAT_MAX, LON_MIN, LON_MAX, WIDTH_MAP, HEIGHT_MAP)
        attraction.draw(p_screen, x - SIZE_IMAGE/2, y - SIZE_IMAGE/2)


def draw_text(screen: pygame.Surface, text: str, position: tuple[int, int], text_color = TEXT_COLOR) -> None:
    font_size = 24
    my_font = pygame.font.SysFont('Arial', font_size)
    text_surface = my_font.render(text, False, text_color)
    
    screen.blit(text_surface, position)