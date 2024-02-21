# Alien colors #1

alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print(f"The alien's color is {color}\n")

# Alien colors #2

for color in alien_color:
    print(f"The alien's color is {color}")
    if color == 'green':
        print('The player just earned 5 points for shooting the alien.\n')
    else:
        print('The player just earned 10 points.\n')

# Alien colors #3 

for color in alien_color:
    print(f"The alien's color is {color}")
    if color == 'green':
        print('The player just earned 5 points for shooting the alien.\n')
    elif color == 'yellow':
        print('The player just earned 10 points.\n')
    elif color == 'red':
        print('The player just earned 15 points.\n')

# Stages of life

ages = [3,1, 78, 49, 7] 

for age in ages:
    print(f"The person's age is {age}")
    if age < 2:
        print('The person is a baby.\n')
    elif age > 1 and age < 4:
        print('The person is a toddler.\n')
    elif age > 3 and age < 13:
        print('The person is a kid.\n')
    elif age > 12 and age < 20:
        print('The person is a teenager.\n')
    elif age > 19 and age < 65:
        print('The person is an adult.\n')
    else:
        print('The person is an elder.\n')    

# 5-9 No Users 

list = []

if len(list) == 0:
    print('We need to find some users!')

for i in range(len(list)):
    list.pop(i)

# 5-10 Checking usernames

current_users = ['user1', 'user2', 'user808', 'user123','JOHn23']
new_users = ['user2','user4','user3','user5','user72834', 'JohN23']

def is_item_in_list(list, item):
    for user in list:
        if item.lower() == user.lower():
            return True

for user in new_users:
    if is_item_in_list(current_users, user):
        print(f'The user {user} already exists.')
    else:
        print(f'The user {user} is available.')

# 5-10 Ordinal numbers

numbers = []

for i in range(9):
    numbers.append(i+1)
    # print(f'The number is {numbers[i]}')
    if(numbers[i]==1):
        print(f'{numbers[i]}st\n')
    elif(numbers[i]==2):
        print(f'{numbers[i]}nd\n')
    elif(numbers[i]==3):
        print(f'{numbers[i]}rd\n')
    else:
        print(f'{numbers[i]}th\n')
        