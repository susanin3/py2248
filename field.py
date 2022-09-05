import random
from copy import copy
import pygame
import drawing
from cell import Cell
import formulas
from colors import Colors


def get_rnd_value():
    return


class Field:
    def __init__(self, screen, cell_size: tuple | list, field_size: tuple | list = (5, 8), cell_margin: int = 3):
        self.screen = screen
        self.cell_size = cell_size
        self.field_size = field_size
        self.cell_margin = cell_margin
        self.field = None
        # c = Cell(screen=screen, position=(0, 0), indexes=(0, 0), size=cell_size, value=2, color=(255, 255, 255))
        # self.field = [[copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)],
        #               [copy(c), copy(c), copy(c), copy(c), copy(c)]]
        self.stack = []
        self.init_values = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)
        # self.init_values = (2048,)
        self.fill_randomly()
        self.selecting = False

    def get_rnd_value(self):
        return self.init_values[random.randint(0, len(self.init_values) - 1)]

    def fill_randomly(self) -> None:
        # for row in range(self.field_size[0]):
        #     for cell in range(self.field_size[1]):
        #         self.field[row][cell] = Cell(position=(0, 0), size=self.cell_size, value=self.init_values[random.randint(0, 6)], color=(255, 255, 255), screen=self.screen)
        self.field = [[Cell(screen=self.screen, position=(0, 0), indexes=(row, cell), size=self.cell_size,
                            value=self.get_rnd_value()) for cell in
                       range(self.field_size[0])] for row in range(self.field_size[1])]

    @staticmethod
    def are_cells_adjacent(c1: Cell, c2: Cell) -> bool:
        return abs(c1.indexes[0] - c2.indexes[0]) <= 1 and abs(c1.indexes[1] - c2.indexes[1]) <= 1

    def adding_valid(self, candidate: Cell) -> bool:
        if candidate.indexes in [i.indexes for i in self.stack]:
            return False
        if len(self.stack) == 0:
            return True
        r = (candidate.value == self.stack[-1].value or candidate.value == self.stack[
            -1].value * 2) and self.are_cells_adjacent(candidate, self.stack[-1])
        if len(self.stack) == 1:
            return r and self.stack[-1].value == candidate.value
        elif len(self.stack) >= 2:
            return r and self.stack[0].value == self.stack[1].value
        # return True

    def draw(self, mouse: pygame.mouse) -> None:
        line_points = [formulas.center(par_pos=i.position, par_size=self.cell_size) for i in self.stack] + [
            mouse.get_pos()]
        if len(line_points) > 1:
            for i in range(len(line_points) - 1):
                drawing.Shape.Line(screen=self.screen, start_point=line_points[i], end_point=line_points[i + 1],
                                   color=self.stack[i].color, width=10).draw()

        x, y = self.cell_margin, self.cell_margin
        for row in self.field:
            x = self.cell_margin
            y += self.cell_size[1] + self.cell_margin
            for cell in row:
                cell.position = (x, y)
                cell.draw()
                x += self.cell_size[0] + self.cell_margin
        # line_points = [i.position for i in self.stack] + [mouse.get_pos()]
        # if len(line_points) > 1:
        # drawing.Shape.Lines(screen=self.screen, points=line_points, color=Colors.White, width=4, closed=False).draw()

    def remove_y0(self, ind):
        self.field[ind[0]][ind[1]] = Cell(screen=self.screen, position=(0, 0),
                                          indexes=(ind[0], ind[1]),
                                          size=self.cell_size,
                                          value=self.get_rnd_value())

    def remove_y(self, cell=None):
        # for i in reversed(list(range(cell.indexes[1]))):
        #     if i == 0:
        #         self.remove_y0()
        for i in self.stack:
            x, y = i.indexes
            self.field[x][y] = None
        self.stack = []

        for r, row in enumerate(self.field):
            for c, cell in enumerate(self.field[r]):
                if cell is None:
                    if r == 0:
                        self.remove_y0((r, c))
                    elif r > 0:
                        self.field[r][c] = self.field[r - 1][c]
                        self.field[r][c].indexes = (r, c)
                        self.field[r - 1][c] = None
                        self.remove_y()

    def sum_and_remove(self):
        vals = [i.value for i in self.stack]
        s = sum(vals)
        last_el = self.stack.pop()
        self.field[last_el.indexes[0]][last_el.indexes[1]].value = formulas.round_to_degree_of_two(s)
        self.field[last_el.indexes[0]][last_el.indexes[1]].determine_color()
        self.remove_y()
        # for i in self.stack:
        #     if i.indexes[0] == 0:
        #         self.remove_y0(i.indexes)
        #     else:
        #         self.remove_y(i)

        # for r, row, in enumerate(self.stack):
        #     for c, cell in enumerate(row):

    def iteration(self, event, mouse: pygame.mouse) -> None:
        pxy = mouse.get_pos()
        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    self.selecting = True
                if ev.button == 3:
                    if len(self.stack) > 1:
                        self.stack.pop()
            if ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    self.selecting = False
        # rmb, lmb = event
        for row in self.field:
            for cell in row:
                if self.selecting:
                    rxy = (cell.position, (cell.position[0] + self.cell_size[0], cell.position[1] + self.cell_size[1]))
                    if formulas.point_occurrence(rxy, pxy) and self.adding_valid(cell):
                        self.stack.append(cell)
                        cell.selected = True
                        # cell.color = Colors.Green
                else:
                    # cell.determine_color()
                    if len(self.stack) > 1:
                        self.sum_and_remove()
                    self.stack.clear()
        self.draw(mouse)
