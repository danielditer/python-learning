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
        
        

    
