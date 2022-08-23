import pygame as pg


class Shape:
    class Rect:
        def __init__(self, color, position, size, width, border_radius, screen):
            self.color = color
            self.position = position
            self.size = size
            self.border_radius = border_radius
            self.width = width
            self.screen = screen

        def draw(self):
            pg.draw.rect(self.screen, color=self.color, width=self.width, border_radius=self.border_radius, rect=(self.position[0], self.position[1], self.size[0], self.size[1]))

    class Line:
        def __init__(self):
            pass


class Text:
    def __init__(self, screen, text, position, color, font):
        self.text = text
        self.position = position
        self.color = color
        self.screen = screen
        self.font = font

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(text_surface, dest=self.position)
