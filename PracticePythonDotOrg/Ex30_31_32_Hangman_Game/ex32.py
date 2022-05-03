# Hangman
from ex31 import displayHangman
from ex30 import getRandomWord


def main():
    words = []
    with open('/PythonStuff/PracticePythonDotOrg/SOWPODS-dict.txt', 'r') as f:
        for line in f:
            words.append(line)
    print('\n               Welcome to hangman!')

    while True:
        randWord = getRandomWord(words)
        displayHangman(randWord)
        retry_input = input('\n Would you like to play again? (y/n) \n > ')
        if retry_input.lower() != 'y':
            print('         Thanks for playing!')
            break
            

if __name__ == '__main__':
    main()