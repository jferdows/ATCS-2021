
class mazebot:
    def __init__(self):
        # location of the boat
        self.x = 1
        self.y = 1

        self.end_x = 3
        self.end_y = 6

        self.current_cell = []*2
        self.visited_cells = []*2

        # location of maze
        self.maze = None

    def move_right(self, node):
        self.x += 1
        self.current_cell[node][0] == self.x
        self.current_cell[node][1] == self.y

    def move_left(self, node):
        self.x-=1
        self.current_cell[node][0] == self.x
        self.current_cell[node][1] == self.y

    def move_up(self, node):
        self.y-=1
        self.current_cell[node][0] == self.x
        self.current_cell[node][1] == self.y

    def move_down(self, node):
        self.y += 1
        self.current_cell[node][0] == self.x
        self.current_cell[node][1] == self.y

    # def have_visited(self):
#         pop current state  & compare ot see if have visited
#          if haven't visited then add to visited set

    def minimax(self):
        self.move_right()


