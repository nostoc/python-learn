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


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = ElectricCar("nisam","leaf",2024)
print(my_leaf.get_descriptive_name())

