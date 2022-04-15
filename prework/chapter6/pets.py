dogs = { 
    'sugar' : {
    'owner' : 'bob',
    'breed' : 'black lab',
    'name' : 'sugar',
},

    'goldie' : {
    'owner' : 'clap',
    'breed' : 'golden retriver',
    'name' : 'goldie'
},

    'earl' : {
    'owner' : 'british',
    'breed' : 'english bulldog',
    'name' : 'earl',
}
}



for dog, dog_info in dogs.items():
    print("The dog " + dog_info['name'].title() + 
    " is a " + dog_info['breed'].title() +
    " and the owner of this dog is " + dog_info['name'].title() + "!")
