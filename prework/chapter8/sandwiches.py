def sandwiches(*items):
    print("\nMaking a sandwich with the following toppings:")

    for layers in items:
        print(layers)

sandwiches('ham', 'cheese')
sandwiches('ham', 'cheese', 'extra toast')
sandwiches('dingleberry')