class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant is called ' + self.restaurant_name + '.')
        print('The restaurant serves ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('The restaurant is open.')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = cuisine_type

    def displayFlavors(self):
        print(self.flavors)

ice_cream = IceCreamStand("Ben and Jerry's", "chocolate, vanilla, strawberry")
ice_cream.displayFlavors()
