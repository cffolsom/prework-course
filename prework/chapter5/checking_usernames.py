current_users = ['bob', 'dave', 'chad', 'dome', 'jeff']

new_users = ['stacy', 'jome', 'yikes', 'CHAD', 'jeff']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("That username of " + new_user + " is already taken")
    else:
        print("You are now a member of this website, " + new_user + "!")