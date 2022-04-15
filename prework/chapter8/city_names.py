def city_county(city, country):
    full_name = city.title() + ', ' + country.title()
    
    print(full_name)

    return full_name.title()

city_county('seattle', 'united states')
city_county('mexico city', 'mexico')
city_county('berlin', 'germany')