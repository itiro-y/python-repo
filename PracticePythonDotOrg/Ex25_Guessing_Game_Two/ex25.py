# Guessing Game Two
# the program will guess the number from 0 to 100
# THIS WAS FUN!

import random

def main():
    machine_guess = random.randint(0, 100)
    new_lower = 0
    new_high = 100
    print('The machine guessed: ', machine_guess)
    while True:
        print('Is the number too low or too high or is it correct? (low, high, nice)?')
        user_input = input('> ')

        if user_input.lower()[0] == 'l':
            new_lower = machine_guess
            machine_guess = random.randint(new_lower, new_high)
            print('new guess!', machine_guess)
        elif user_input.lower()[0] == 'h':
            new_high = machine_guess
            machine_guess = random.randint(new_lower, new_high)
            print('new guess!', machine_guess)
        elif user_input.lower()[0] == 'n':
            print('The machine got it right!')
            break
        else:
            print('Invalid Input. Try Again')
            break

if __name__ == '__main__':
    main()