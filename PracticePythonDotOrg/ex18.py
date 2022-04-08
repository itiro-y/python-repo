# Cows And Bulls

import random

def main():
    while True:
        winner = False
        gen_4d_num = str(random.randint(1000,9999))
        print(gen_4d_num)

        while not winner:
            user_input = str(input('Enter a number: \n > '))
            winner = cowsAndBullsGame(user_input, gen_4d_num)
    
        print(f'Winner!. the generated number was {gen_4d_num}')
        game_loop = str(input('Would you like to play again? (y/n) \n > '))

        if(game_loop.lower() != 'y'):
            break


def cowsAndBullsGame(get_num, get_rand_num):
    cows = 0
    bulls = 0
    for i in range(len(get_num)):
        if get_num[i] == get_rand_num[i]:
            cows += 1
        else:
            bulls += 1
    print(f'{cows} cows, {bulls} bulls')
    if(cows == 4):
        return True
    else:
        return False


if __name__ == '__main__':
    main()