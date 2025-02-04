class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"The name of the restaurant is  {self.name}, and it has {self.cuisine_type} type cuisine."
        )

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open now..")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["vanilla","chocolate","oreo biscuit"]
        
    def get_flavors_list(self):
        for flavor in self.flavors:
            print({flavor})

my_icecream = IceCreamStand("Dimashi","Buffet")
my_icecream.get_flavors_list()
