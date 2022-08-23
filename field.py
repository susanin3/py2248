import pygame

from cell import Cell
import formulas


class Field:
    def __init__(self, screen, cell_size: tuple | list, field_size=(5, 8), cell_margin=3):
        self.cell_size = cell_size
        self.cell_margin = cell_margin
        c = Cell(position=(0, 0), size=cell_size, value="VAL", color=(255, 255, 255), screen=screen)
        self.field = [[c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c],
                      [c, c, c, c, c]]
        self.stack = []

    def draw(self):
        x, y = self.cell_margin, self.cell_margin
        for row in self.field:
            x = self.cell_margin
            y += self.cell_size[1] + self.cell_margin
            for cell in row:
                cell.position = (x, y)   # ПОМЕНЯТЬ НА ИНДЕКСИРОВАНИЕ
                cell.draw()
                x += self.cell_size[0] + self.cell_margin

    def iteration(self, mouse: pygame.mouse):
        for row in self.field:
            for cell in row:
                rxy = (cell.position, (cell.position[0] + self.cell_size[0], cell.position[1] + self.cell_size[1]))
                pxy = mouse.get_pos()
                if formulas.point_occurrence(rxy, pxy):
                    print(cell.position)
        self.draw()
