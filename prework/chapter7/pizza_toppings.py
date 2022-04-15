prompt = "\nHello, what kind of topping would you like to order?"
prompt += "\n(Enter 'quit' to cease the program)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping.title() + " has been added to the pizza.")