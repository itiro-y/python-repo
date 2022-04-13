from ex30 import getRandomWord

# Guess Letters
# Hangman

def main():
    words = []
    with open('/PythonStuff/PracticePythonDotOrg/SOWPODS-dict.txt', 'r') as f:
        for line in f:
            words.append(line)
    word = str(getRandomWord(words))
    print(">>>Welcome to Hangman!")
    displayHangman(word)
    

def displayHangman(word):
    word_len = len(word)
    word_update = ['_' for x in range(word_len)]
    guesses = 0
    previous_guess = ''
    game_display = 'This is your word: ' + ('_ ' * word_len)
    print(game_display)
    while True:
        char_index = []
        word = word.lower()
        last_index = 0
        hangman = hangmanPicture()
        print(hangman[guesses][0])
        user_input = input('        >>> Guess your letter: ')
        for i in range(word_len):
            if word[i] == user_input:
                char_index.append(word.find(user_input, last_index, word_len))
                last_index = i + 1

        for i in range(word_len):
            for j in range(len(char_index)):
                if i == char_index[j]:
                    word_update[char_index[j]] = user_input

        print('         ' + ' '.join(word_update))
    
        word_string = ''.join(word_update)
        if previous_guess != user_input:    
            guesses += 1
            previous_guess = user_input

        if  word_string.strip() == word:
            print('That is correct!')
            break
        elif guesses == 6:
            print('You are out of guesses! GAME OVER')
            break


def hangmanPicture():
    hangman = [["""
                    |><><|
                    0    |
                         |
                         | 
                ========== """],
                ["""
                    |><><| 
                    0    |
                    |    |
                         |
                ========== """],
                ["""
                    |><><|
                    0    |
                   -|    |
                         |
                ========== """],
                ["""
                    |><><|
                    0    |
                   -|-   |
                         |
                ========== """],
                ["""
                    |><><|
                    0    |
                   -|-   |
                   /     |
                ========== """],
                ["""
                    |><><|
                    0    |
                   -|-   |
                   / \\   |
                ========== """]]   
    return hangman


if __name__ == '__main__':
    main()