pizzas = ['cheese', 'pepperonis', 'extra cheesy']
for pizza in pizzas:
    print("I like " + pizza + " pizza!")
print("I really like pizza, they make me fat and thicker! I mainly go for cheesey pizzas and such. Pepperoni is okay if the company making them is the bomb. I god damn love pizza, holy cow.\n")

friend_pizzas = pizzas[:]

pizzas.append('vegen')
friend_pizzas.append('meat lover')

for pizza in pizzas:
    print("My updated list also has " + pizza + " pizzas!")

print("\n")

for friend_pizza in friend_pizzas:
    print("My friend also likes " + friend_pizza + " pizzas!")