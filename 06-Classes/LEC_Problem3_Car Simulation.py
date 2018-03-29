class Car():


    def __init__(self, efficiency=11, fuel_tank=0):
        self.fuel_tank = fuel_tank
        self.efficiency = efficiency


    def refuel(self, litres):
        self.fuel_tank += litres
        return 'Your car has ' + str(self.fuel_tank) + ' litres of gas.'


    def drive(self, distance):
        self.drive = distance
        return 'Your car travelled ' + str(self.drive)


    def fuel_left(self, distance):
        if self.fuel_tank <= 0:
            return 'You don\'t have enough in your tank. Please refuel.'
        self.drive = distance
        self.fuel_tank = self.fuel_tank - (self.drive/self.efficiency)
        return 'Fuel left: ' + str(self.fuel_tank) + ' litres'

my_car = Car()
print(my_car.refuel(50))
print(my_car.refuel(50))
print(my_car.drive(225))
print(my_car.fuel_left(225))
