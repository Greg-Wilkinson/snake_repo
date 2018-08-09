# https://stackoverflow.com/questions/40649634/determine-length-of-keypress-in-python
from snake import Snake
from board import Board

##########################################################
import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab

fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
ax.plot([1, 2, 4])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

##########################################################

import pygame
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Time")
clock = pygame.time.Clock()

pygame.init()

clock = pygame.time.Clock()

boa = Snake
myBoard = Board(10,30)

frame = 0
running = True
while running:
    frame +=1
    print("Frame Number: " + str(frame))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # key 'w'
                boa.direction = "UP"
            elif event.key == pygame.K_s: # key 's'
                boa.direction = "Down"
            elif event.key == pygame.K_a: # key 'a'
                boa.direction = "LEFT"
            elif event.key == pygame.K_d: # key 'd'
                boa.direction = "RIGHT"

            boa.move()
            head = boa.positions[0]

            cond1 = (boa.positions[0] >= 0)
            cond2 = (boa.positions[1] >= 0)
            cond3 = (boa.positions[0] < myBoard.height)
            cond4 = (boa.positions[1] < myBoard.width)

            if cond1 and cond2 and cond3 and cond4:
                pass
            else:
                running = False

        screen.fill((255, 255, 255))
        pygame.display.update()

        clock.tick(40)
