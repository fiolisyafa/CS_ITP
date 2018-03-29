def make_car(manufacturer, model, **car_info):
    car = {}
    car['Manufacturer'] = manufacturer
    car['Model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

my_car = make_car('VW', 'Beetle', color='Yellow', feature='Sunroof')
print(my_car)
