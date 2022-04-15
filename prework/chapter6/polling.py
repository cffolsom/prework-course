favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'steven': 'python',
    'ultimate dave': 'everything',

}

people = ['steven', 'ultimate dave', 'stacy', 'numbah', 'monkee']

for person in people:
    if person in favorite_languages.keys():
        print("Thank you for taking our poll, " + person.title() + "!")
    else:
        print("You should take our polls, " + person.title() + ".")

##if 'erin' not in favorite_languages.keys():
##    print("Erin, please take our poll!")

##friends = ['phil', 'sarah']
##for name in favorite_languages.keys():
##    print(name.title())
##
##    if name in friends:
##        print(" Hi " + name.title() +
##        ",I see your favorite language is " +
##        favorite_languages[name].title() + "!")

##for name in sorted(favorite_languages.keys()):
##    print(name.title() + ", thank you for taking the poll.")

##print("The following languages have been mentioned:")
##or language in set(favorite_languages.values()):
##   print(language.title())