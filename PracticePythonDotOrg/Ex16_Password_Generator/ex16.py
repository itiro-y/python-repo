# Password Generator
# ascii codes
# 32 - 47, 58 - 64, 91 -96, 123 - 126 are symbols
# 48 - 57 are numbers
# 65 - 90 are uppercase letters
# 97 - 122 are lowercase letters

import random

def main():
    weak_pw = genWeapPw()
    strong_pw = genStrongPW()
    print('Here is your weak password: ', weak_pw)
    print('here is your strong password: ', strong_pw)

def genWeapPw():
    temp_str = ''
    words = """banana melon mug bottle newspaper 
               cube toy monitor internet book chair"""
    words_list = words.split()
 
    for i in range(2):
        rnd_index = random.randint(1, len(words_list) - 1)
        temp_str += words_list[rnd_index]
    return temp_str

def genStrongPW():
    strong_pw = ''

    for i in range(random.randint(1, 10)):
        symbol_str = genRandSymbol()
        letter_str = genRandLetter()
        num_str = str(random.randint(0, 10))
        strong_pw += ''.join(unifyAndShuffleStr(symbol_str, letter_str, num_str))

    return strong_pw

def genRandLetter():
    letter_str = ''
    letters_list = [random.randint(65, 90), random.randint(97, 122)]
    letter_str = chr(letters_list[random.randint(1, len(letters_list) - 1)])
    return letter_str

def genRandSymbol():
    symbol_str = ''
    symbols_list = [random.randint(32, 47), 
                    random.randint(58, 64),
                    random.randint(91, 96),
                    random.randint(123, 126)]
    symbol_str += chr(symbols_list[random.randint(1, len(symbols_list) - 1)])
    return symbol_str

def unifyAndShuffleStr(get_symbol, get_letter, get_number):
    unify_list = [get_symbol, get_letter, get_number]
    random.shuffle(unify_list)
    return unify_list

if __name__ == '__main__':
    main()