# Tic Tac Toe Game

from ex24 import drawBoard
from ex27 import userInputTTT


def main():
    while True:
        print('Welcome to the Tic Tac Toe Game!')
        initial_board = drawBoard()
        userInputTTT(initial_board[0], initial_board[1])
        user_input = input('Would you like to play again? (y or n) \n >')
        if user_input.lower() != 'y':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    main()