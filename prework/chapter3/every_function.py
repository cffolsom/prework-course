#an attempt to use every function covered in chapter 3
print("This is the original list.")
list = ['English', 'Dutch', 'Swiss', 'Spanish', 'Mexican']
print(list)

print("\nThis is the original list sorted.")
print(sorted(list))

print("\nThis is the original list sorted but in reverse.")
print(sorted(list, reverse=True))

print("\nThis is the original list for clarity.")
print(list)

print("\nPosition 0 is popped.")
popped_position = list.pop(0)
print(list)

print("\nPosition 3 is removed.")
list.remove('Spanish')
print(list)

print("\nA new language is appended")
list.append('Japanese')
print(list)

print("\nAforementioned language is deleted.")
del list[3]
print(list)

print("\nList is sorted permenantly.")
list.sort()
print(list)
