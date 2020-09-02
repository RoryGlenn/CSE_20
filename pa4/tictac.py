# assignment: programming assignment 4
# author: Rory Glenn
# date: 8/2/20
# file: tictac.py runs the main game loop that accepts user input
# input: choose a cell A1-C3
# output: prints whos turn it is

from random import choice

from pa4.board import Board
from pa4.player import Player, AI, SmartAI

# from board import Board
# from player import Player, AI, SmartAI

print("Welcome to TIC-TAC-TOE Game!")

while True:

    board = Board()

    #player1 = Player("Bob", "X")
    player1 = AI("Bob", "X", board)

    # player2 = Player("Alice", "O")
    player2 = SmartAI("Alice", "O", board)
    turn = True

    while True:
        board.show()

        if turn:
            player1.choose(board)
            # player2.remove_cell(player1.cell)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break

    board.show()

    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")

    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")

    else:
        print("It is a tie!")

    ans = input("Would you like to play again? [Y/N] ").upper()

    if ans != "Y":
        break

print("Goodbye!")
