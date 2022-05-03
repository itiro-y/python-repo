# String List
# Ask the user for a string and print out whether this string is a palindrome 
# or not. (A palindrome is a string that reads the same forwards and backwards.)

def main():
    user_input = str(input('Enter a word: '))
    # First approach

    # input_length = len(user_input) - 1
    # i = 0

    # while True:
    #     if user_input[i] != user_input[input_length]:
    #         print('It is not a palindrome')
    #         break

    #     input_length -= 1
    #     i += 1
    #     if i == input_length | i > input_length:
    #         print('It is a palindrome')
    #         break
    
    # Second, better approach
    reversed_input = user_input[::-1]
    if user_input == reversed_input:
        print('yes')
    else:
        print('no')        

if __name__ == '__main__':
    main()