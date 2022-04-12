# Check Tic Tac Toe

from ex24 import drawBoard

def main():
    # drawBoard()

    # 0 means its empty
    # 1 means player 1 token
    # 2 menas player 2 token
    board_now = [[1, 2, 1], 
                 [1, 0, 2], 
                 [1, 2, 1]]
    checkWinner(board_now)

# winning conditions full row or column or diagonal
def checkWinner(board_list):
    if board_list[0][0] == board_list[0][1] == board_list[0][2]:
        if board_list[0][0] == 1:
            print('p1 wins by row')
            return True
        elif board_list[0][0] == 2:
            print('p2 wins by row')
            return True
    elif board_list[1][0] == board_list[1][1] == board_list[1][2]:
        if board_list[1][0] == 1:
            print('p1 wins by row')
            return True
        elif board_list[1][0] == 2:
            print('p2 wins by row')
            return True
    elif board_list[2][0] == board_list[2][1] == board_list[2][2]:
        if board_list[2][0] == 1:
            print('p1 wins by row')
            return True
        elif board_list[2][0] == 2:
            print('p2 wins by row')
            return True
    elif board_list[0][0] == board_list[1][0] == board_list[2][0]:
        if board_list[0][0] == 1:
            print('p1 wins by column')
            return True
        elif board_list[0][0] == 2:
            print('p2 wins by column')
            return True
    elif board_list[0][1] == board_list[1][1] == board_list[2][1]:
        if board_list[0][1] == 1:
            print('p1 wins by column')
            return True
        elif board_list[0][1] == 2:
            print('p2 wins by column')
            return True
    elif board_list[0][2] == board_list[1][2] == board_list[2][2]:
        if board_list[0][2] == 1:
            print('p1 wins by column')
            return True
        elif board_list[0][2] == 2:
            print('p2 wins by column')
            return True
    elif board_list[0][0] == board_list[1][1] == board_list[2][2]:
        if board_list[0][0] == 1:
            print('p1 wins by diagonal')
            return True
        elif board_list[0][0] == 2:
            print('p2 wins by diagonal')
            return True
    else:
        return False

if __name__ == '__main__':
    main()