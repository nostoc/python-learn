class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name =name
        self.age = age
        
    def sit(self):
        """Simulating a dog sitting in reponse to a command"""
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """Simulate dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")
        
        

my_dog = Dog("Rockey",12)
print(f"My dog is {my_dog.name}. He is {my_dog.age} years old.")
my_dog.roll_over()
my_dog.sit()
