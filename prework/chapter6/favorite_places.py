places = {
    'brandon' : ['missouri', 'his basement'],
    'mafew' : ['missouri', 'his dnd room', 'his jojo house'],
    'sam' : ['mississippi', 'anywhere with grace'],
}

for name, locations in places.items():
    print("\n" + name.title() + "'s favorite places are the following:")
    for place in locations:
        print("\t" + place.title())