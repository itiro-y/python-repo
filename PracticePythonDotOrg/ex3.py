# List Less Than Ten


my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
temp_list = []
user_num = int(input('Give me a number to check: '))
print(f'Numbers from my_list that are lass than {user_num}: ')
    
for i in my_list:
    if i < user_num:
        temp_list.append(i)
   
temp_list.sort()
print(temp_list)

