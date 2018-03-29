class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant is called ' + self.restaurant_name + '.')
        print('The restaurant serves ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('The restaurant is open.')

restaurant = Restaurant('Pizza Hut', 'Italian')
restaurant2 = Restaurant('Fish n Co', 'seafood')
restaurant3 = Restaurant('Holy Cow', 'Steak')
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
