def car_info(manufacturer, model_name, **other_info):

    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model name'] = model_name
    for key, value in other_info.items():
        car_profile[key] = value
    return car_profile

total_info = car_info('honda', 'corvette', year='25', condition='good')

print(total_info)