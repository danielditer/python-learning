# 7-1 Rental Car
print("# 7-1 Rental Car")
car = input("Enter the model of the car you want to rent: ")
print(f"Let me see if I can find you a {car}")

# 7-2 Restaurant Seating
print("# 7-2 Restaurant Seating")
number_persons = input("How many people are in your dinner group?: ")
number_persons = int(number_persons)
if number_persons > 8:
    print("You'll have to wait for a table!")
else:
    print("Your table is ready!")

# 7-3 Multiples of Ten
print("# 7-3 Restaurant Seating ")
number = input("Enter the number: ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is multiple of 10.")
else:
    print(f"The number {number} is not multiple of 10."):