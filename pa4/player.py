# assignment: programming assignment 4
# author: Rory Glenn
# date: 8/2/20
# file: player.py gets and sets the players name and cell they choose to move to
# input: choose a cell A1-C3
# output: nothing

from random import choice


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.cell = ""

    def get_sign(self):
        return self.sign

    # return an instance sign
    def get_name(self):
        return self.name

    # return an instance name
    def choose(self, board):
        while True:
            cell_choice = input(self.name + ", " + self.sign + ":" + " Enter a cell [A-C][1-3]:")
            self.cell = cell_choice
            # check if the cell_choice is valid, if so then don't loop
            if board.set(cell_choice, self.sign) != -1:
                break


# AI plays as Bob
class AI(Player):
    def __init__(self, name, sign, board):
        Player.__init__(self, name, sign)
        self.name = name
        self.sign = sign
        self.all_possible_moves = ['A1', 'B1', 'C1',
                                   'A2', 'B2', 'C2',
                                   'A3', 'B3', 'C3']

    def choose(self, board):

        print("Bob, X: Enter a cell [A-C][1-3]:")

        while True:

            empty_slots = list()

            i = 0
            while i < 9:
                if board.isempty(i):
                    empty_slots.append(i)
                i += 1

            cell_choice = self.all_possible_moves[choice(empty_slots)]

            if board.set(cell_choice, self.sign) is not -1:
                break


class SmartAI(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        self.isFirstMove = False

    def choose(self, board):

        print("Alice, O: Enter a cell [A-C][1-3]:")

        if self.isFirstMove == False:
            self.make_first_move(board)
            board.turns += 1
            return

        if self.check_two_matching_diagonal(board):
            board.turns += 1
            return

        if self.check_two_matching_row(board):
            board.turns += 1
            return

        if self.check_two_matching_column(board):
            board.turns += 1
            return

        if self.check_single_matching(board):
            board.turns += 1
            return

        # last resort if conditions above weren't met
        if board.isempty(0):
            board.board[0] = 'O'
        elif board.isempty(2):
            board.board[2] = 'O'
        elif board.isempty(6):
            board.board[6] = 'O'
        elif board.isempty(8):
            board.board[8] = 'O'

        board.turns += 1

        if board.turns == 9 and board.winner is "":
            print("It is a tie!")


    def check_two_matching_diagonal(self, board):

        """ When finding a matching two, I believe it is better to think offensively first
            rather than defensively because if the SmartAI thinks offensively first, they
            can win the game."""

        # Offensive

        # left -> right diagonal
        if board.board[0] == 'O' and board.board[4] == 'O' and board.isempty(8):
            board.board[8] = 'O'
            return True

        elif board.board[4] == 'O' and board.board[8] == 'O' and board.isempty(0):
            board.board[0] = 'O'
            return True

        elif board.board[0] == 'O' and board.board[8] == 'O' and board.isempty(4):
            board.board[4] = 'O'
            return True


        # right -> left diagonal
        elif board.board[2] == 'O' and board.board[4] == 'O' and board.isempty(6):
            board.board[6] = 'O'
            return True

        elif board.board[4] == 'O' and board.board[6] == 'O' and board.isempty(2):
            board.board[2] = 'O'
            return True

        elif board.board[2] == 'O' and board.board[6] == 'O' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # Defensive

        # left -> right diagonal
        elif board.board[0] == 'X' and board.board[4] == 'X' and board.isempty(8):
            board.board[8] = 'O'
            return True
        elif board.board[4] == 'X' and board.board[8] == 'X' and board.isempty(0):
            board.board[0] = 'O'
            return True
        elif board.board[0] == 'X' and board.board[8] == 'X' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # right -> left diagonal
        elif board.board[2] == 'X' and board.board[4] == 'X' and board.isempty(6):
            board.board[6] = 'O'
            return True
        elif board.board[4] == 'X' and board.board[6] == 'X' and board.isempty(2):
            board.board[2] = 'O'
            return True
        elif board.board[2] == 'X' and board.board[6] == 'X' and board.isempty(4):
            board.board[4] = 'O'
            return True

        return False

    def check_two_matching_row(self, board):

        # Offensive

        # row 1
        if board.board[0] == 'O' and board.board[1] == 'O' and board.isempty(2):
            board.board[2] = 'O'
            return True
        elif board.board[1] == 'O' and board.board[2] == 'O' and board.isempty(0):
            board.board[0] = 'O'
            return True
        elif board.board[0] == 'O' and board.board[2] == 'O' and board.isempty(1):
            board.board[1] = 'O'
            return True

        # row 2
        elif board.board[3] == 'O' and board.board[4] == 'O' and board.isempty(5):
            board.board[5] = 'O'
            return True
        elif board.board[4] == 'O' and board.board[5] == 'O' and board.isempty(3):
            board.board[3] = 'O'
            return True
        elif board.board[3] == 'O' and board.board[5] == 'O' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # row 3
        elif board.board[6] == 'O' and board.board[7] == 'O' and board.isempty(8):
            board.board[8] = 'O'
            return True
        elif board.board[7] == 'O' and board.board[8] == 'O' and board.isempty(6):
            board.board[6] = 'O'
            return True
        elif board.board[6] == 'O' and board.board[8] == 'O' and board.isempty(7):
            board.board[7] = 'O'
            return True

        # Defensive

        # row 1
        elif board.board[0] == 'X' and board.board[1] == 'X' and board.isempty(2):
            board.board[2] = 'O'
            return True

        elif board.board[1] == 'X' and board.board[2] == 'X' and board.isempty(0):
            board.board[0] = 'O'
            return True

        elif board.board[0] == 'X' and board.board[2] == 'X' and board.isempty(1):
            board.board[1] = 'O'
            return True

        # row 2
        elif board.board[3] == 'X' and board.board[4] == 'X' and board.isempty(5):
            board.board[5] = 'O'
            return True

        elif board.board[4] == 'X' and board.board[5] == 'X' and board.isempty(3):
            board.board[3] = 'O'
            return True

        elif board.board[3] == 'X' and board.board[5] == 'X' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # row 3
        elif board.board[6] == 'X' and board.board[7] == 'X' and board.isempty(8):
            board.board[8] = 'O'
            return True

        elif board.board[7] == 'X' and board.board[8] == 'X' and board.isempty(6):
            board.board[6] = 'O'
            return True

        elif board.board[6] == 'X' and board.board[8] == 'X' and board.isempty(7):
            board.board[7] = 'O'
            return True

        return False

    def check_two_matching_column(self, board):

    # Offensive

        # column 1
        if board.board[0] == 'O' and board.board[3] == 'O' and board.isempty(6):
            board.board[6] = 'O'
            return True
        elif board.board[3] == 'O' and board.board[6] == 'O' and board.isempty(0):
            board.board[0] = 'O'
            return True
        elif board.board[0] == 'O' and board.board[6] == 'O' and board.isempty(3):
            board.board[3] = 'O'
            return True

        # column 2
        elif board.board[1] == 'O' and board.board[4] == 'O' and board.isempty(7):
            board.board[7] = 'O'
            return True
        elif board.board[4] == 'O' and board.board[7] == 'O' and board.isempty(1):
            board.board[1] = 'O'
            return True
        elif board.board[1] == 'O' and board.board[7] == 'O' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # column 3
        elif board.board[2] == 'O' and board.board[5] == 'O' and board.isempty(8):
            board.board[8] = 'O'
            return True
        elif board.board[5] == 'O' and board.board[8] == 'O' and board.isempty(2):
            board.board[2] = 'O'
            return True
        elif board.board[2] == 'O' and board.board[8] == 'O' and board.isempty(5):
            board.board[5] = 'O'
            return True

        # Defensive

        # column 1
        elif board.board[0] == 'X' and board.board[3] == 'X' and board.isempty(6):
            board.board[6] = 'O'
            return True
        elif board.board[3] == 'X' and board.board[6] == 'X' and board.isempty(0):
            board.board[0] = 'O'
            return True
        elif board.board[0] == 'X' and board.board[6] == 'X' and board.isempty(3):
            board.board[3] = 'O'
            return True

        # column 2
        elif board.board[1] == 'X' and board.board[4] == 'X' and board.isempty(7):
            board.board[7] = 'O'
            return True
        elif board.board[4] == 'X' and board.board[7] == 'X' and board.isempty(1):
            board.board[1] = 'O'
            return True
        elif board.board[1] == 'X' and board.board[7] == 'X' and board.isempty(4):
            board.board[4] = 'O'
            return True

        # column 3
        elif board.board[2] == 'X' and board.board[5] == 'X' and board.isempty(8):
            board.board[8] = 'O'
            return True
        elif board.board[5] == 'X' and board.board[8] == 'X' and board.isempty(2):
            board.board[2] = 'O'
            return True
        elif board.board[2] == 'X' and board.board[8] == 'X' and board.isempty(5):
            board.board[5] = 'O'
            return True

        return False

    def check_single_matching(self, board):

        # row 1
        if (board.board[0] == 'O' or board.board[2] == 'O') and board.isempty(1):
            board.board[1] = 'O'
            return True

        # row 2
        elif (board.board[3] == 'O' or board.board[5] == 'O') and board.isempty(4):
            board.board[4] = 'O'
            return True

        # row 3
        elif (board.board[6] == 'O' or board.board[8] == 'O') and board.isempty(7):
            board.board[7] = 'O'
            return True

        # column 1
        elif (board.board[0] == 'O' or board.board[6] == 'O') and board.isempty(3):
            board.board[3] = 'O'
            return True

        # column 2
        elif (board.board[1] == 'O' or board.board[7] == 'O') and board.isempty(4):
            board.board[4] = 'O'
            return True

        # column 3
        elif (board.board[2] == 'O' or board.board[8] == 'O') and board.isempty(5):
            board.board[5] = 'O'
            return True

        # right to left diagonal
        elif (board.board[2] == 'O' or board.board[6] == 'O') and board.isempty(4):
            board.board[4] = 'O'
            return True

        # left to right diagonal
        elif (board.board[0] == 'O' or board.board[8] == 'O') and board.isempty(4):
            board.board[4] = 'O'
            return True

    def make_first_move(self, board):

        # figures out what the players first move was
        i = 0
        opponents_first_move = 0
        while i < 9:
            if not board.isempty(i):
                opponents_first_move = i
                break
            i += 1

        # we want out first move to be in the center of the board
        if opponents_first_move is not 4:
            board.board[4] = 'O'

        # if we can't move in the center of the board, pick a random corner
        elif opponents_first_move is 4:
            random_corner = [0, 2, 6, 8]
            board.board[choice(random_corner)] = 'O'

        self.isFirstMove = True
