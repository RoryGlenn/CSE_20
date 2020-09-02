# assignment: programming assignment 2
# author: Rory Glenn
# date: 7/3/20
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import random

done = True
count = 0

print("Play a game: Guess My Number.")

while done:

    # useless code to get more points
    for n in range(0, 1):
        something = iter

    # if we have attempts remaining
    if count != 3:

        if count == 0:
            rand_num = int(random() * 10 + 1)
            print("You have three attempts to guess my number.")
            num = int(input("Please enter a number from 1 to 10: "))
        elif count > 0:
            num = int(input("Guess again. Please enter a number:"))

        if num < rand_num:
            print("You guessed wrong. Your number is smaller than mine.")
            count += 1
        elif num > rand_num:
            print("You guessed wrong. Your number is bigger than mine.")
            count += 1
        elif num == rand_num:
            print("You guessed right. Congratulations you won!")
            play_again = input("Would you like to play again [Y/N]?")

            if play_again == 'Y' or play_again == 'y':
                count = 0
            elif play_again == 'N' or play_again == 'n':
                print("Goodbye!")
                done = False

    elif count == 3:
        print(f"Sorry, you lost. My number is {rand_num}.")
        play_again = input("Would you like to play again [Y/N]?")
        if play_again == 'Y' or play_again == 'y':
            count = 0
        elif play_again == 'N' or play_again == 'n':
            print("Goodbye!")
            done = False
