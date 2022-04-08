# Fibonacci

def main():
    user_input = int(input('How many items in fibonacci? \n > '))
    for i in range(user_input):
        print(fibonacciRec(i))


def fibonacci(num):
    temp_list = []
    if num == 0:
        print('Cannot be 0. Invalid input')
        return
    else: 
        for i in range(num):
            if i == 0:
                temp_list.append(0)
            if i == 1:
                temp_list.append(1)    
            if i > 1:
                temp_list.append(temp_list[i - 1] + temp_list[i - 2])
    return temp_list

# Recursive
def fibonacciRec(num):
    if num <= 1:
        return num
    else:
        return (fibonacciRec(num - 1) + fibonacciRec(num - 2))


if __name__ == '__main__':
    main()