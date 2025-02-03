class Car:
    """A simple attempt to model a car"""
    def __init__(self, make, year, model):
        """Initializing attributes"""
        self.make = make
        self.year = year
        self.model = model
        self.odoeter_reading = 0
        
    def get_gescriptive_name(self):
        descriptive_name = print(f"{self.make} {self.year} {self.model} ")
        return descriptive_name
    
    def read_odometer(self):
        print(f"{self.odoeter_reading}")
    
    def update_odometer(self,new_odometer_reading):
        if new_odometer_reading > self.odoeter_reading:
            self.odoeter_reading = new_odometer_reading
        else:
            print("You can't roll back odometer reading")
    
    def increase_odometer_reading(self,increament):
        self.odoeter_reading += increament

    
my_car = Car("Audi", year=2024,model="a4",)
my_car.get_gescriptive_name()
my_car.update_odometer(45)
my_car.increase_odometer_reading(2)
my_car.read_odometer()