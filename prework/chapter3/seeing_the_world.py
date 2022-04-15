#This is another list but has the sort and sorted fuction in it with some verations of reversing.
list = ['Germany', 'Austria', 'Ukraine', 'Japan', 'United Kingdoms']
print("Original list.")
print(list)

print("\nSorted List.")
print(sorted(list))

print("\nSorted list in reverse.")
print(sorted(list, reverse=True))

print("\nThe list is back to its original order")
print(list)

print("\nSorted list permenantly in reverse.")
list.reverse()
print(list)

print("\nSorted list reversed back to original.")
list.reverse()
print(list)

print("\nThe list is back to its ordered list but permenantly")
list.sort()
print(list)

print("\nSorted list permenantly in reverse, again.")
list.sort(reverse=True)
print(list)