def city_country(city, country):
    """Return the city and country names"""
    cityncountry = city + ',' + ' ' + country
    return cityncountry

city = city_country('Jakarta', 'Indonesia')
print(city)
city = city_country('Shanghai', 'China')
print(city)
city = city_country('Dublin', 'Ireland')
print(city)
