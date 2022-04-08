# This program generates a random number fom 0 to 9 and prompts
# the user to guess it.
# Ayrton Itiro Kobo Yoshii 30.03.2022

import random

MAX_NUMBERS = 3

def main():
    print("A number has been generated. Can you guess it? (0-9)")
    while True:
        rand_num = getRandNum()
        print('What is your guess ')
        user_guess = input('> ')

        isGuessCorrect(user_guess, rand_num)
        print('Would you like to try again? (yes or no)')
        user_prompt = input('> ')
        
        if user_prompt[0].lower() != 'y':    
            break       

def getRandNum():
    num_range = list('0123456789')
    random.shuffle(num_range)
    return num_range[0]

def isGuessCorrect(user_guess, rand_num):
    if not user_guess.isdecimal():
        print('invalid input')
    elif user_guess == rand_num:
        print('correct answer')
    else:
        print(f'incorrect, it was {rand_num} try again')

if __name__ == '__main__':
    main()


    