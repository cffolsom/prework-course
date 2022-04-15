##username_list = ['bob', 'manny', 'dave', 'admin', 'warden']
username_list = []
if username_list:
    for name in username_list:
        if name == 'admin':
            print("Admin login")
        elif name in username_list:
            print("Generic login")
else:
    print("We need more users!")
