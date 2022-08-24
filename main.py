import sys
import datetime as dt
import pygame as pg
from cell import Cell
from colors import Colors
from field import Field
import drawing

"""
play field size: 5x8 cells
"""

pg.init()
size = width, height = 600, 900
cell_size = (60, 60)
black = (0, 0, 0)
white = (255, 255, 255)
screen = pg.display.set_mode(size)
# surface = pg.Surface()
clock = pg.time.Clock()
font = pg.font.Font(pg.font.get_default_font(), 20)
font.underline = Colors.WhiteSmoke
field = Field(screen=screen, cell_size=cell_size, cell_margin=10)
score = drawing.Text(screen=screen, text="0", position=(10, 10), color=Colors.Snow, font=font)

while 1:
    screen.fill(black)
    clock.tick(60)
    events = pg.event.get()
    for event in events:
        # print(event)
        if event.type == pg.KEYDOWN:
            if event.key == 27:
                sys.exit()
        if event.type == pg.QUIT:
            sys.exit()

    score.draw()
    field.iteration(mouse=pg.mouse, event=events)
    # text_surface = font.render(f"{dt.datetime.now()}", True, white)
    # screen.blit(text_surface, dest=(0, 0))
    # pg.display.flip()
    pg.display.update()
