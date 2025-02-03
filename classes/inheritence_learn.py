class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_ododmtere(self, milege):
        if milege > self.odometer_reading:
            self.odometer_reading = milege
        else:
            print("You can't roll back an odomter!")

    def increament_odometer(self, increament):
        self.odometer_reading += increament
    
    def fill_gas_tank(self, tank_amount):
        self.tank_amount = tank_amount
        print(f"Gas tank is {self.tank_amount} amount filled.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40
        
    def describe_battery(self):
        print(f"{self.get_descriptive_name()} has a battery of size, {self.battery_size}")  
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car does not have a gas tank!") 
        
my_leaf = ElectricCar("nisam","leaf",2024)
print(my_leaf.get_descriptive_name())
print(my_leaf.describe_battery())
print(my_leaf.fill_gas_tank())

