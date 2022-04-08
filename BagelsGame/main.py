import random

NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
    print('''I am thinking of a 3-digit number. Try to guess what it is')
    Here are some clues: '
    When I say   That means: 
        Pico     One digit is correct but in the wrong position
        Fermi    One digit is correct and in the right position
        Bagels   No digit is correct
    I have thought of a number.
    You have 10 guesses to get it. ''')
    while True:
        secret_num = getSecretNum()
        num_guess = 1
        while num_guess <= NUM_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guess}')
                guess = input('> ')

                clues =  getClues(guess, secret_num)
                print(clues)
                num_guess += 1

                if guess == secret_num:
                    break
                if num_guess > NUM_GUESSES:
                    print('You ran out of guesses')
                    print(f'Your answer was {secret_num}')
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

        print('Thanks for playing!')


def getSecretNum():
    numbers = list('123456789')
    random.shuffle(numbers)
    secret_num = ''

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    return secret_num


def getClues(guess, secret_num):
    if(guess == secret_num):
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi ')
        elif guess[i] in secret_num:
            clues.append('Pico ')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)   


if __name__ == '__main__':
    main()





