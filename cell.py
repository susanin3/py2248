import pygame as pg
import drawing


class Cell:
    def __init__(self, position, size, value, color, screen):
        self.position = position
        self.size = size
        self.value = value
        self.color = color
        self.screen = screen

    def draw(self):
        drawing.Shape.Rect(position=self.position, size=self.size, color=self.color, width=0, border_radius=10, screen=self.screen).draw()
        # pg.draw.rect(screen, color=self.color, width=0, border_radius=10, rect=(self.position[0], self.position[1], 50, 50))
