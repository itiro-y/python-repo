# Check Primality Functions

def main():
    user_num = int(input('Enter a number: \n > '))
    
    if isPrime(user_num):
        print('The number is prime')
    else:
        print('The number is NOT prime')    

def isPrime(num):
    temp_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            temp_list.append(i)
      
    if len(temp_list) == 0:
        return False        
    elif temp_list[0] == 1:
        if len(temp_list) == 1:
            return True
        elif temp_list[1] == num:
            return True 
    else:
        return False            

if __name__ == '__main__':
    main()
