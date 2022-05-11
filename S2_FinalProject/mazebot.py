from cell import Cell

class Mazebot:
    def __init__(self):
        self.current_cell = None

        self.maze = []
        self.path = []


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
        self.fill_maze_cells(int_maze)


    # adding cells to maze
    # determines start & stop points in array & walls
    def fill_maze_cells(self, int_maze):
        # int_maze = mazebot.load_maze("maze1.txt")
        for row in range(len(int_maze)):
            temp_row = []
            for col in range(len(int_maze[0])):
                cell = Cell()
                cell.row = row
                cell.col = col
                if (int_maze[row][col] == 1):
                    cell.wall = True
                else:
                    cell.wall = False
                    if (int_maze[row][col] == 2):
                        self.start_row = row
                        self.start_col = col
                        cell.is_in_path = True
                    elif (int_maze[row][col] == 3):
                        self.end_row = row
                        self.end_col = col
                temp_row.append(cell)
            self.maze.append(temp_row)


    # prints maze
    def print_maze(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                cell = self.maze[row][col]
                if (cell.row == self.current_cell.row and cell.col == self.current_cell.col):
                    print("X", end="")
                elif (cell.wall):
                    print("1", end="")
                else:
                    print("0", end="")
            print()


    # implements breadth first search to traverse maze
    def BFS(self, maze):
        to_visit = []
        cell = maze[self.start_row][self.start_col]

        while (not(cell.row == self.end_row and cell.col == self.end_col)):
            # checking cell to the right
            next_cell = maze[cell.row][cell.col + 1]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True
            # checking cell below
            next_cell = maze[cell.row + 1][cell.col]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True
           # checking cell to the left
            next_cell = maze[cell.row][cell.col - 1]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True
            # checking cell above
            next_cell = maze[cell.row - 1][cell.col]
            if (next_cell.visited == False and next_cell.wall == False):
                to_visit.append(next_cell)
                next_cell.parent = cell
                cell.visited = True
            cell = to_visit.pop(0)
        #storing cells of most efficient path in array
        while(not(cell.row == self.start_row and cell.col == self.start_col)):
            cell.is_in_path = True
            self.path.append(cell)
            cell = cell.parent
        self.path.append(cell)

    # prints mazebot's path in maze
    def solve_maze(self):
        self.BFS(self.maze)
        for i in range (len(self.path)-1, -1, -1):
            self.current_cell = self.path[i]
            self.print_maze()
            print()




if __name__ == '__main__':
    mazebot = Mazebot()
    mazebot.load_maze("maze1.txt")
    mazebot.solve_maze()

