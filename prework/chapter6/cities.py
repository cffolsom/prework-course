cities = {
    'seattle' : {
        'country' : 'usa',
        'population' : '120 million',
        'facts' : 'this city has a lot of homeless people sadly',

    },
    'berlin' : {
        'country' : 'germany',
        'population' : '1 trillion',
        'facts' : 'berlin is berlin',
    },
    'tokyo' : {
        'country' : 'japan',
        'population' : '2 million',
        'facts' : 'tokyo is the home of the free',
    },
}

for country, info in cities.items():
    print("The city of " + country.title() +
    " is in " + info['country'].title() +
    " with a population of " + info['population'] + ". " +
    "\nAlso, here's a cool fact about this city: " +
    info['facts'] + ".")