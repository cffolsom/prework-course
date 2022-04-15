#a list of people that has been changed.
list = ['Bob', 'Jimmy', 'Dan']
print(list)

message = " is cordinally invited to dinner this night."
print(list[0] + message)
print(list[1] + message)
print(list[2] + message)

print("\nHowever " + list[0] + " cannot make it.")
del list[0]
list.insert(0, 'Nanny')
print("\n" + list[0] + message)
print(list[1] + message)
print(list[2] + message)

print("\n" + "Good news, everyone! I just brought a bigger dining table!")

list.insert(0, 'Peter')
list.append('Monster')
list.insert(2, 'Brian')

print("\n" + list[0] + message)
print(list[-1] + message)
print(list[2] + message)

print("\n" + "Bad news, everyone! My table won't arrive in time and I hate all of you except two very specific people.")

list_popped = list.pop(0)
print("\nSorry " + list_popped + " but you have lost the lottery and you are uninvited.")
list_popped = list.pop(0)
print("Sorry " + list_popped + " but you have lost the lottery and you are uninvited.")
list_popped = list.pop(0)
print("Sorry " + list_popped + " but you have lost the lottery and you are uninvited.")
list_popped = list.pop(0)
print("Sorry " + list_popped + " but you have lost the lottery and you are uninvited.")

print("Don't worry, " + list[0] + ", you are still invited!")
print("Don't worry, " + list[1] + ", you are still invited!")

del list[0]
del list[0]
print(list)