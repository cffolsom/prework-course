words = 'Yikes'
lc_test = 'Zoinks'
age_0 = 20
age_1 = 17
list_items = ['one', 'two']
number = 'three'
number_one = 'one'
if words != 'Wowee':
    print("Yikes, amigos! The answer is: ")
    print(words == 'Wowee')

if words == 'Yikes':
    print("Yikes, amigos! The answer is: ")
    print(words == 'Yikes')

if lc_test.lower() == 'zoinks':
    print("This is a lowercase test.")

if lc_test.lower() != 'zoinks':
    print("This is a lowercase test.")

if age_0 >= 19:
    print("True")

if age_0 >= 21 or age_1 <= 16:
    print("False")

if number not in list_items:
    print("True")

if number_one not in list_items:
    print("False")
