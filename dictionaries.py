# 6-1 Person

person = { 
    'first_name': 'daniel', 
    'last_name': 'caballero',
    'age': 36,
    'city': 'Cochabamba'
    }

for k, v in person.items():
    print(f'My {k} is {str(v).capitalize()}')

# 6-2 Favorite Number

favorite_numbers = {
    'sarah': 45,
    'ann': 23,
    'joseph': 324,
    'phil': 42,
    'brandon': 12,
    'john': 7890
}

print('\n#6-2 Favorite Number')
for k, v in favorite_numbers.items():
    print(f'My name is {k.capitalize()} and my favorite number is {v}')

river = {
    'nile': 'Egypt',
    'amazonas': 'Brazil',
    'mississippi': 'USA',
}

print('\n#6-5 Rivers')
for k,v in river.items():
    print(f'The {k.capitalize()} runs through {v}')

print('\n#River countries')
for k in river.keys():
    print(f'{k.capitalize()}')

print('\n#Rivers')
for k in river.values():
    print(f'{k}')

#6-6 Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'brandon': 'python',
    'john': 'c',
}

#6-7 People
person2 = {
    'first_name': 'jack',
    'last_name': 'smith',
    'age': 23,
    'city': 'New York'
    }

person3 = {
    'first_name': 'sarah',
    'last_name': 'brandon',
    'age': 42,
    'city': 'Washington'
}

people = [person, person2, person3]

print('\n6-7 People')
for person in people:
    print(f'\n{person["first_name"].title()}:')
    for k, v in person.items():
        print(f'My {k.replace("_"," ").title()} is {str(v).title()}')