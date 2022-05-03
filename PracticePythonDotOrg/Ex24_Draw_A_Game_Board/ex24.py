# Draw a Game Board
# A board is has always the same amount of rows and columns (3x3, 4x4, 5x5)

def main():
    refreshBoard([[0,0,0], [0,0,0], [0,0,0]])
    drawBoard()

def drawBoard():
    print("Let's define your board (x,y)!")
    board_x = int(input('Enter a value for x: \n > '))
    board_y = int(input('Enter a value for y: \n > '))
    board_coord = [board_x, board_y]
    board = ''
    for rows in range(board_y):
        board += board_x * ' ---'
        board += '\n'
        board += (board_x) * '| 0 '
        board += '|\n'
    print('\n --This is your board--')    
    print(board)
    print('0s stands for empty spaces')
    print('1s stands for player 1')
    print('0s stands for player 2 \n')
    return board_coord

def refreshBoard(board_list):
    board = ''
    board_x = len(board_list)
    board_y = board_x

    for i in range(board_y):
        j = 0
        board += board_x * ' ---'
        board += '\n'
        while j < board_x:
            board += '| ' + str(board_list[i][j]) + ' '
            j += 1
        board += '|\n'
    print(board)


if __name__ == '__main__':
    main()

