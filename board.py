class Board(object):

    def __init__(self, width, height):
        if width < 6:
            width = 6
        if height < 6:
            height = 6
        self.height = height
        self.width = width