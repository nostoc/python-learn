class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is  {self.name}, and it has {self.cuisine_type} type cuisine.")
        
    def open_restaurant(self):
        print(f"The {self.name} restaurant is open now..")
        

restaurant =  Restaurant("Covanro", "Buffet")
print(f"Restaurant {restaurant.name} has {restaurant.cuisine_type} type cuisine.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("Dimashi", "Fried rice")
restaurant3 = Restaurant("Seven Say", "Whatever")
print("\n")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()