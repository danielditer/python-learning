# Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('The first three elements in the list are:')
for player in players[:3]:
    print(player.title())

print('The last three elements in the list are:')
for player in players[-3:]:
    print(player.title())