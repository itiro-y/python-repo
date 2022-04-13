# Functions Refactor
# Same code as one of the functions of ex24

def main():
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
    

if __name__ =='__main__':
    main()