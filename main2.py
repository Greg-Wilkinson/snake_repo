from pygame.locals import *
import pygame

from snake import Snake
from board import Board
#
boa = Snake
myBoard = Board(10, 30)

class Player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
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

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                boa.direction = "RIGHT"

            if (keys[K_LEFT]):
                boa.direction = "LEFT"

            if (keys[K_UP]):
                boa.direction = "UP"

            if (keys[K_DOWN]):
                boa.direction = "DOWN"

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()