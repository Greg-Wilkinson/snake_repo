class Snake(object):

    def __init__(self):
        self.alive = True
        self.positions = [[0, 2], [0, 1], [0, 0]]

    def move(self, direction):
        head = self.positions[0]
        if self.direction == "UP":
            new_pos = [head[0] + 1, head[1]]
        elif self.direction == "DOWN":
            new_pos = [head[0] - 1, head[1]]
        elif self.direction == "LEFT":
            new_pos = [head[0], head[1] - 1]
        elif self.direction == "RIGHT":
            new_pos = [head[0], head[1] + 1]

        self.positions = self.positions[:-1]
        self.positions = [new_pos] + self.positions