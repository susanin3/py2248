import math
import pygame as pg
import drawing
import formulas
from colors import Colors


class Cell(object):
    def __init__(self, screen, position: tuple | list, indexes: tuple | list, size: tuple | list, value: int):
        self.screen = screen
        self.position = position
        self.indexes = indexes
        self.size = size
        self.value = value
        self.color = None
        self.selected = False
        self.determine_color()

    def determine_color(self) -> None:
        self.color = Colors.stack[int(math.log2(self.value) % len(Colors.stack))]

    def draw(self) -> None:
        font = pg.font.Font(pg.font.get_default_font(), 15)
        drawing.Shape.Rect(position=self.position, size=self.size, color=self.color, width=0, border_radius=10, screen=self.screen).draw()
        drawing.Text(screen=self.screen, text=f"{self.value}", position=formulas.center(par_pos=self.position, par_size=self.size), color=Colors.Black, font=font).draw()
        # drawing.Text(screen=self.screen, text=f"{self.indexes}", position=(self.position[0], self.position[1] + 20), color=Colors.Black, font=font).draw()
        # pg.draw.rect(screen, color=self.color, width=0, border_radius=10, rect=(self.position[0], self.position[1], 50, 50))
