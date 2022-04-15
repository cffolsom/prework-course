sandwich_orders = ['bacon sandwiches', 'pastrami', 'pastrami' 'ham sandwiches', 'tuna sandwich', 'pastrami']
finished_orders = []

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_order = sandwich_orders.pop()
    print("Currently making: " + current_order.title())
    print("\nAlso we are currently out of Pastrami!")

    finished_orders.append(current_order)


print("The current list of orders are as it follows: ")
for sandwich_order in finished_orders:
    print(sandwich_order.title())
