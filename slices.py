# Slices
players = ['charles', 'martina', 'michael', 'a','b','florence', 'eli']
print('The first three elements in the list are:')
for player in players[:3]:
    print(player.title())

print('The last three elements in the list are:')
for player in players[-3:]:
    print(player.title())

print('The items from the middle of the list are:')
for player in players[int(len(players)/2)+1-2:int(len(players)/2)+2]:
    print(player.title())