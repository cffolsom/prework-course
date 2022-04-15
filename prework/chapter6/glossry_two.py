glossary = {
    'boolean': "returns as true or false",
    'tuple': "a value that cannot be changed",
    'if' : "starts an if statement",
    'dictionary': "holds a bunch of keys and values",
    'str': "a string"
}

for key, value in glossary.items():
    print("A " + key.title() + " has the following action of " + value + ".")