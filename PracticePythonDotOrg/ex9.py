# Guessing Game One

import random

x = random.randint(1,9)
print(x)
while True:
    y = int(input("guess the number (1-9): \n > "))
    if y == x:
        print("You got it!")
        break
    elif y > x:
        print("Your guess is too high")
    elif y < x:
        print("Your guess is too low")  
    else:
        print("Invalid input")
        break          
    