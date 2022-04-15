prompt = "\nEnter your age, the ticket price changes depending on it."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    elif int(age) <= 3:
        print("Your ticket costs nothing!")
    elif int(age) >= 3 and int(age) <= 12:
        print("Your ticket costs $10")
    else:
        print("Your ticket costs $15")