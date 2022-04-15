favorite_numbers = {
    'bob': [5, 20],
    'stacy': [30, 10, 2],
    'jimmy': [23, 3],
    'chad': [112221312341, 1337],
    'ben': [30, 1],
}

for name, numbers in favorite_numbers.items():
   print(name.title() + "'s favorite numbers are: ")
   for value in numbers:
        print("\t" + str(value))
