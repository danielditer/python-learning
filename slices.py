# Slices
players = ['charles', 'martina', 'michael', 'a','b','florence', 'eli']
print('The first three elements in the list are:')
for player in players[:3]:
    print(player.title())

print('The last three elements in the list are:')
for player in players[-3:]:
    print(player.title())

print('The items from the middle of the list are:')
for player in players[int(len(players)/2)-1:int(len(players)/2)+2]:
    print(player.title())

#pizzas
pizzas = ['Margherita','Pepperoni','Hawaiian','Veggie Supreme','BBQ Chicken', 'Pesto and Tomato']

pizzas_copy = pizzas[:]

pizzas.append('pizza1')
pizzas_copy.append('pizza2')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in pizzas_copy:
    print(friend_pizza)
