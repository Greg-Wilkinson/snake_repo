class Player:

    step = 50
    x = [2*step, step, 0]
    y = [0, 0, 0]
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self):
        # pass
        # self.length = 3
        # initial positions, no collision.
        self.blah = 1

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            head = self.positions[0]
            if self.direction == "UP":
                new_pos = [head[0] + self.step, head[1]]
            elif self.direction == "DOWN":
                new_pos = [head[0] - self.step, head[1]]
            elif self.direction == "LEFT":
                new_pos = [head[0], head[1] - self.step]
            elif self.direction == "RIGHT":
                new_pos = [head[0], head[1] + self.step]

            self.x = self.x[:-1]
            self.y = self.y[:-1]
            self.x = [new_pos[0]] + self.y
            self.y = [new_pos[1]] + self.x
        return

    def moveRight(self):
        self.direction = "RIGHT"

    def moveLeft(self):
        self.direction = "LEFT"

    def moveUp(self):
        self.direction = "UP"

    def moveDown(self):
        self.direction = "DOWN"

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
