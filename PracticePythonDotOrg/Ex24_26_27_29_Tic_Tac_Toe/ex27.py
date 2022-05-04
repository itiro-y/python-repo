# Tic Tac Toe Draw
# player 1 starts
from ex24 import refreshBoard
from ex26 import checkWinner

def main():
    userInputTTT(3, 3)

def userInputTTT(x_coord, y_coord):
    game_board = [ [0]*y_coord for i in range(x_coord)]
    count = 0
    while True:
        print('What is your play, PLAYER 1? ')
        user_input_row = int(input('Enter a row: \n > '))
        user_input_col = int(input('Enter a column: \n > '))
        if game_board[user_input_row][user_input_col] == 0:
            game_board[user_input_row][user_input_col] = 1
            refreshBoard(game_board)
            if checkWinner(game_board):
                break
            count += 1
        else:
            print('the spot is already taken, lost your turn')

        if count == 9:
            break

        print('What is your play, PLAYER 2? ')
        user_input_row = int(input('Enter a row: \n > '))
        user_input_col = int(input('Enter a column: \n > '))
        if game_board[user_input_row][user_input_col] == 0:
            game_board[user_input_row][user_input_col] = 2
            refreshBoard(game_board)
            if checkWinner(game_board):
                break
            count += 1
        else:
            print('the spot is already taken, lost yor turn')

        if count == 9:
            break
    if count == 9:
        print('There are no more moves')

if __name__ == '__main__':
    main()
