responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name here: ")
    location = input("What would be your dream vacation? ")

    responses[name] = location

    repeat = input("Is there anyone else who wishes to use this poll (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("Poll results...")
for name, instance in responses.items():
    print(name + ": " + instance)

