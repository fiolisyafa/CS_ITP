class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served


    def describe_restaurant(self):
        print('The restaurant is called ' + self.restaurant_name + '.')
        print('The restaurant serves ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('The restaurant is open.')

    def set_number_served(self, numberserved):
        self.number_served = numberserved
        return self.number_served

    def increment_number_served(self, add_number_served):
        self.number_served += add_number_served
        return self.number_served

restaurant = Restaurant('Pizza Hut', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
print(restaurant.set_number_served(5))
print(restaurant.increment_number_served(10))

