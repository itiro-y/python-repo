# Pick Word
import random

def main():
    words = []
    with open('/PythonStuff/PracticePythonDotOrg/SOWPODS-dict.txt', 'r') as f:
        for line in f:
            words.append(line)
    print(getRandomWord(words))


def getRandomWord(word_list):
    max_count = len(word_list)
    rand_index = random.randint(0, max_count)
    return word_list[rand_index].strip()


if __name__ == '__main__':
    main()