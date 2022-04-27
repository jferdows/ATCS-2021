from mazebot import mazebot

class cell:
    def __init__(self):
        mb = mazebot()

        self.x = mazebot.self.x
        self.y = mazebot.self.x
        self.curr_cell = None

        self.visited = []

    def current_cell (self):
        if (self.y == 1):
            self.curr_cell = self.x-1
        elif(self.y == 2):
            self.curr_cell = 5+1
        elif (self.y == 3):
            self.curr_cell = 8+1
        self.visited.add(self.curr_cell)

