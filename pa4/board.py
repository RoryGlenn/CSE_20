# assignment: programming assignment 4
# author: Rory Glenn
# date: 8/2/20
# file: board.py contains the data structure to get and set board movement
# input: choose a cell A1-C3
# output: prints board to console


class Board:

    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        self.winner = ""
        self.tie = False
        self.turns = 0

    def get_size(self):
        return self.size

    # return the board size (an instance size)
    def get_winner(self):
        return self.winner

    # return the winner (a sign O or X) (an instance winner)
    def set(self, cell, sign):

        converted_cell = self.convert_cell(cell)

        if converted_cell is not -1:
            if self.isempty(converted_cell):
                self.board[converted_cell] = sign
                self.turns += 1
            else:
                # space is not empty
                print("You did not choose correctly.")
                return -1
        else:
            return -1

    # mark the cell with the sign (X or O)
    def isempty(self, converted_cell):
        if self.board[converted_cell] != ' ':
            return False
        return True

    # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonals()
        self.check_tie()

        if self.tie:
            return True

        if self.winner is not "":
            return True

        return False

    # draw the board
    def show(self):
        print("")
        print("   A   B   C")
        print(" +---+---+---+")
        print("1| " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " |")
        print(" +---+---+---+")
        print("2| " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " |")
        print(" +---+---+---+")
        print("3| " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " |")
        print(" +---+---+---+")

    def convert_cell(self, cell):
        if cell == 'A1' or cell == 'a1':
            return 0
        elif cell == 'B1' or cell == 'b1':
            return 1
        elif cell == 'C1' or cell == 'c1':
            return 2
        elif cell == 'A2' or cell == 'a2':
            return 3
        elif cell == 'B2' or cell == 'b2':
            return 4
        elif cell == 'C2' or cell == 'c2':
            return 5
        elif cell == 'A3' or cell == 'a3':
            return 6
        elif cell == 'B3' or cell == 'b3':
            return 7
        elif cell == 'C3' or cell == 'c3':
            return 8
        else:
            print("You did not choose correctly.")
            return -1

    def check_diagonals(self):
        if self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
            self.winner = 'X'
        elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
            self.winner = 'X'

        elif self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
            self.winner = 'O'
        elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
            self.winner = 'O'

    def check_rows(self):
        if self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
            self.winner = 'X'
        elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
            self.winner = 'X'
        elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
            self.winner = 'X'

        elif self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
            self.winner = 'O'
        elif self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
            self.winner = 'O'
        elif self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
            self.winner = 'O'

    def check_columns(self):
        if self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
            self.winner = 'X'
        elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
            self.winner = 'X'
        elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
            self.winner = 'X'

        elif self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
            self.winner = 'O'
        elif self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
            self.winner = 'O'
        elif self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
            self.winner = 'O'

    # tie condition - all board spaces are full and there is no 3 in a row
    def check_tie(self):
        if self.turns == 9 and self.winner is "":
            self.tie = True

    def get_board(self):
        return self.board
