# Reverse Word Order

def main():
    user_input = str(input('Enter a phrase: \n > '))
    reversePhrase(user_input)

def reversePhrase(get_string):
    temp_list = get_string.split()
    temp_string = ''
    
    for i in range(len(temp_list) - 1, -1, -1):
        temp_string += temp_list[i] + ' '
    print(temp_string)

if __name__ == '__main__':
    main()