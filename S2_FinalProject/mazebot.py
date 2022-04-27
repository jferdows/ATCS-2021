
class mazebot:
    def __init__(self):
        # location of the boat
        self.x = None
        self.y = None

        self.path = []

        # location of maze
        self.maze = None

    def move_right(self):
        self.x += 1
        self.path.append('r')

    def move_left(self):
        self.x-=1
        self.path.append('l')

    def move_up(self):
        self.y-=1
        self.path.append('u')

    def move_down(self):
        self.y += 1
        self.path.append('d')



