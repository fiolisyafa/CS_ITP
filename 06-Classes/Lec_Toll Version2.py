class Vehicle():

    def __init__(self, category):
        self.category = category


class Car(Vehicle):

    def __init__(self):
        super().__init__('car')

class Bus(Vehicle):

    def __init__(self):
        super().__init__('bus')


class Truck(Vehicle):

    def __init__(self):
        super().__init__('truck')


class Toll():
    def __init__(self, car_fee, bus_fee, truck_fee, location='Senayan'):
        self.fee_category = {'car': car_fee, 'bus': bus_fee, 'truck': truck_fee}
        self.location = location
        self.carcount = 0
        self.buscount = 0
        self.truckcount = 0
        self.revenue = 0

    def charge(self, vehicle):
        if isinstance(vehicle, Car):
            self.revenue += self.fee_category['car']
            return self.fee_category['car']
        elif isinstance(vehicle, Bus):
            self.revenue += self.fee_category['bus']
            return self.fee_category['bus']
        elif isinstance(vehicle, Truck):
            self.revenue += self.fee_category['truck']
            return self.fee_category['truck']

    def vehicle_count(self, vehicle):
        if isinstance(vehicle, Car):
            self.carcount += 1
        if isinstance(vehicle, Bus):
            self.buscount += 1
        if isinstance(vehicle, Truck):
            self.truckcount += 1

    def final_revenue(self):
        return self.revenue

    def final_vehicle_count(self):
        return self.carcount, self.buscount, self.truckcount


toll_gate = Toll(6000, 8000, 10000)

print('=========================\nToll Payment Systems\nPT Jasamarga TBK\n=========================')
while True:
    vehicle_type = input('Category of Vehicle\n1. Car (RP %d)\n2. Bus (RP %d)\n3. Truck (RP %d)' % (toll_gate.fee_category['car'], toll_gate.fee_category['bus'], toll_gate.fee_category['truck']))
    if vehicle_type.lower() == 'car':
        vehicle = Car()
    if vehicle_type.lower() == 'bus':
        vehicle = Bus()
    if vehicle_type.lower() == 'truck':
        vehicle = Truck()

    toll_gate.vehicle_count(vehicle)
    fee = toll_gate.charge(vehicle)
    print('\nFee: %d' %fee)

    print('\nAny more vehicles? Y/N')
    more_vehicles = input()
    if more_vehicles.upper() == 'N':
        vehicle_count = toll_gate.final_vehicle_count()
        print('=========================\nCar\t\tBus\t\tTruck\n=========================')
        print('%d\t\t%d\t\t%d' % (vehicle_count[0], vehicle_count[1], vehicle_count[2]))
        print('=========================')
        total_revenue = toll_gate.final_revenue()
        print('Revenue: ' + str(total_revenue))
        break
    else:
        pass
