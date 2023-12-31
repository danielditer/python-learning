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
