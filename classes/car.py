class Car:
    """A simple attempt to model a car"""
    def __init__(self, make, year, model):
        """Initializing attributes"""
        self.make = make
        self.year = year
        self.model = model
        self.odoeter_reading =0
        
    def get_gescriptive_name(self):
        descriptive_name = print(f"{self.make} {self.year} {self.model} ")
        return descriptive_name
    
    def read_odometer(self):
        print(f"{self.odoeter_reading}")
    
    
my_car = Car("Audi", year=2024,model="a4")
my_car.get_gescriptive_name()