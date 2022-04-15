def show_magicians(magician_name):
    for name in magician_name:
        print(name.title() + " is a magician.")

def make_great(old_name, great_name):
    while old_name:
       making_great = old_name.pop() + ' the Great'
       great_name.append(making_great)


names = ['bob', 'jim', 'nuts']
great_names = []

make_great(names, great_names)
show_magicians(great_names)
