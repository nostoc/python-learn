class User:
    def __init__(self,first_name,last_name,**user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        
    def describe_user(self):
        print(f"First name : {self.first_name}\nLast name : {self.last_name}")
        print("\nOther information of user")
        print(f"{self.user_info}")
      
    
    def greet_user(self):
        print(f"Hello, {self.first_name}")
       
            
            
hansika = User("Hansika","Karunathilake",age=23,university="UoR",boy_friend="Janitha")
hansika.describe_user()