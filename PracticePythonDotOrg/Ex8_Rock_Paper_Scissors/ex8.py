# Rock Paper Scissors

def main():
    while True:
        player1 = input('Rock, Paper or Scissor? \n > ')
        player2 = input('Rock, Paper or Scissor? \n > ')
        check = '' 

        if player1.isalpha() & player2.isalpha():
            if player1 == player2:
                print('ITS A DRAW \n')
            else:    
                if didPlayerOneWin(player1, player2):
                    print('PLAYER 1 WINS \n')
                else:
                    print('PLAYER 2 WINS \n')  

            check = input('Would you like to keep playing the game? (y/n) \n > ')
            if check[0].lower() != 'y':
                print('Thanks for playing the game!')
                break
        else:
            print('Invalid Input. Quitting the game...')
            break            
            

def didPlayerOneWin(player1, player2):
    p1 = convertInputToInt(player1)
    p2 = convertInputToInt(player2)

    if p1 == 1:
        if p2 == 2:
            return True
        else:
            return False
    elif p1 == 2:
        if p2 == 1:
            return False
        else:
            return True
    elif p1 == 3:
        if p2 == 1:
            return True
        else:
            return False
    else:
        return                         
 

def convertInputToInt(input):
    if input == 'rock':
        return 1
    elif input == 'scissors':
        return 2
    else:
        return 3  # 'paper'  
     
if __name__ == '__main__':
    main()