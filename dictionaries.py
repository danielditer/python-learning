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
for k, v in river.items():
    print(f'The {k.capitalize()} runs through {v}')

print('\n#River countries')
for k in river.keys():
    print(f'{k.capitalize()}')

print('\n#Rivers')
for k in river.values():
    print(f'{k}')

# 6-6 Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'brandon': 'python',
    'john': 'c',
}

# 6-7 People
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
        print(f'My {k.replace("_", " ").title()} is {str(v).title()}')

# 6-8 Pets

pet1 = {'name': 'Max', 'owner': 'John', 'type': 'dog'}
pet2 = {'name': 'Nala', 'owner': 'Charlie', 'type': 'cat'}
pet3 = {'name': 'Kiwi', 'owner': 'Sarah', 'type': 'bird'}
pet4 = {'name': 'Luna', 'owner': 'Joseph', 'age': '', 'type': 'dog'}
pet5 = {'name': 'Charlie', 'owner': 'Jennifer', 'age': '', 'type': 'dog'}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f'\n{pet["name"].title()}:')
    for k, v in pet.items():
        print(f'My {k.title()} is {str(v).title()}')

# 6-9 Favorite Places

favorite_places = {
    'jen': ['house', 'college', 'museum'],
    'sarah': ['gym', 'mall'],
    'edward': ['house', 'gym', 'zoo']
}

for k, v in favorite_places.items():
    print(f'My name is {k.title()} and my favorite places are:')
    for i, place in enumerate(v, start=1):
        print(f'{i}.{place.title()}')

# 6-11 Cities

cities = {
    'chicago': {
        'country': 'USA',
        'population': '2.7 million',  # As of around 2021
        'fact': 'Chicago is known for its significant contributions to the fields of music (especially jazz and blues), architecture, and its deep-dish pizza.'
    },
    'los angeles': {
        'country': 'USA',
        'population': '4 million',  # As of around 2021
        'fact': 'Los Angeles is home to Hollywood, a major center of the world entertainment industry, and is known for its Mediterranean climate.'
    },
    'new york': {
        'country': 'USA',
        'population': '8.4 million',  # As of around 2021
        'fact': 'New York City is often called “The Big Apple” and is famous for its cultural diversity, Broadway shows, and being a financial hub.'
    },
}

print("\n# 6-11 Cities")
for k, v in cities.items():
    print(f"{k.title()} is a city from {v['country'].title()} it's population is {v['population']} and a fact of "
          f"this city is {v['fact']}")

