responses = {}
#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the user's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store the response in the dictionary.
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person repond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")