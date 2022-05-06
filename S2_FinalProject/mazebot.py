from cell import Cell

class Mazebot:
    def __init__(self):
        # location of the boat
        self.start_x = 1
        self.start_y = 1

        self.end_x = 3
        self.end_y = 6

        self.current_cell = None
        self.poss_cells = []

        # array of maze
        self.maze = []

    # load the maze file
    # fill maze with cells
    def load_maze(self, file):
        int_maze = []
        with open(file) as f:
            line = f.readline().strip()
            while line:
                line = [int(char) for char in line]
                int_maze.append(line)
                line = f.readline().strip()
        # print(int_maze)

        self.fill_maze_cells(int_maze)


    # determining what spots in array are walls
    # adding cells to maze
    def fill_maze_cells(self, int_maze):
        # int_maze = mazebot.load_maze("maze1.txt")
        for row in range(len(int_maze)):
            temp_row = []
            for col in range(len(int_maze[0])):
                cell = Cell()
                cell.x = row
                cell.y = col
                if (int_maze[row][col] == 1):
                    cell.wall = True
                else:
                    cell.wall = False
                temp_row.append(cell)
            self.maze.append(temp_row)


    def print_maze(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                cell = self.maze[row][col]
                if (cell.wall == True):
                    print("1", end="")
                else:
                    print("0", end="")
            print("")


    def BFS(self, maze):
        to_visit = []
        path = []
        cell = maze[self.start_x][self.start_y]

        while (not(cell.x == self.end_x and cell.y == self.end_y)):

            # checking cell to the right
            next_cell = maze[self.start_x + 1][self.start_y]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True

           # checking cell below
            next_cell = maze[self.start_x][self.start_y - 1]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True

            # checking cell to the left
            next_cell = maze[self.start_x - 1][self.start_y]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True

            # checking cell above
            next_cell = maze[self.start_x][self.start_y + 1]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True

            cell = to_visit[0]

        #getting x & y coordinates of cells of most efficient path
        i = 0
        while(cell.parent.x != 1 and cell.parent.y != 1):
            path[i][0] = cell.parent.x
            path[i][1] = cell.parent.y
            i+=1
        return path


    def solve_maze(self):
        path = self.BFS(self.maze)
        for i in range(len(path)):
                x_coord = path.pop[i][0]
                y_coord = path.pop[i][1]
                self.maze[x_coord][y_coord] = "X"
                print(self.maze)


if __name__ == '__main__':
    mazebot = Mazebot()
    mazebot.load_maze("maze1.txt")
    mazebot.solve_maze()

