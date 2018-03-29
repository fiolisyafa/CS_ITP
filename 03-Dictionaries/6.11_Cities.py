cities = {
    "Canberra": {
        "country": "Australia",
        "population": "6573",
        "fact": "Capital city but nothing interesting happens."
        },
    "London": {
        "country": "England",
        "population": "5673",
        "fact": "Harry Potter grew up here."
        },
    "Jakarta": {
        "country": "Indonesia",
        "population": "903659306239659302",
        "fact": "Not livable."
        },
    }
for city, information in cities.items():
    print(city + ":")
    country = information["country"]
    population = information["population"]
    fact = information["fact"]
    print('\t' + "Located in", country)
    print('\t' + "Has a population of", population, "people")
    print('\t' + fact)

