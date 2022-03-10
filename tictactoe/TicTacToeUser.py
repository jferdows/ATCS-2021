import random

class TicTacToeUser:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        for i in range(3):
            self.board.append(['-', '-', '-'])


    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe! \n")
        print("Player 1 is X and Player 2 is 0 \n")
        print("Take turns placing your pieces - the first to 3 in a row wins!")


    def print_board(self):
        # TODO: Print the board
        print("\t" + str(0) + "\t" + str(1) + "\t" + str(2))
        for i in range(3):
            print(str(i) + "\t" + self.board[i][0] + "\t" + self.board[i][1] + "\t" + self.board[i][2])


    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        isValidMove = False
        if (row >= 0 and row < 3 and col >= 0 and col < 3):
            if self.board[row][col] == '-':
                isValidMove = True
        return isValidMove


    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player


    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = int(input("Enter a row: "))
        col = int(input("Enter a column: "))
        while (self.is_valid_move(row, col) == False):
            print("Please enter a valid move.")
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))
        self.place_player(player, row, col)


    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        self.take_manual_turn(player)


    def check_col_win(self, player):
        # TODO: Check col win
        colWin = False
        for col in range(3):
            if(self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player):
                    colWin = True
        return colWin


    def check_row_win(self, player):
        # TODO: Check row win
        rowWin = False
        for row in range(3):
            if (self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player):
                rowWin = True
        return rowWin


    def check_diag_win(self, player):
        # TODO: Check diagonal win
        win = False
        num_diag = 0
        for i in range(3):
            if self.board[i][i] == player:
                num_diag += 1
        if (num_diag == 3):
            win = True
        return win


    def check_win(self, player):
        # TODO: Check win
        win = False
        if (self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            win = True
        return win


    def check_tie(self):
        # TODO: Check tie
        # Check board full
        isTie = True
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    isTie = False

        if (self.check_win("X") or self.check_win("O")):
            isTie = False
        return isTie


    def play_game(self):
        # TODO: Play game
        isGoing = True
        while (isGoing):
            self.print_board()
            self.take_turn("X")
            if (self.check_win("X")):
                print("X Won! GAME OVER")
                break
            if (self.check_tie()):
                print("It's a tie! GAME OVER")
                break

            self.print_board()
            self.take_turn("O")
            if (self.check_win("O")):
                print("O Won! GAME OVER")
                break
            if (self.check_tie()):
                print("It's a tie! GAME OVER")
                break