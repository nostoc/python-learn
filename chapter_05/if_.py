# cars = ["audi","bmw","ferrari","bugati"]
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# car = "maruti"
# print("Is Car == 'Maruti'? I predict true")
# print(car =="maruti")

# banned_users = ["janitha","chamuditha","dhanuja"]
# user_ = "irushi"
# if user_ in banned_users:
#     print(f"{user_}, you are banned.")
# else:
#     print(f"{user_}, you are a good user.")
    
    

# age = 22
# if age>23 or age<=30:
#     print("Authorized")
# else:
#     print("Unauthorized")
    
# age = 12
# if age<4:
#     print("$4")
# elif age <18:
#     print("$25")
# else:
#     print("$40")
    
# alien_color = "yellow"

# if(alien_color=="green"):
#     print("You earnerd 5 points!")
# elif(alien_color=="yellow"):
#     print("You earnerd 10 points!")
# elif(alien_color=="red"):
#     print("You earned 15 points!")
# age = 65
# if(age<2):
#     print("baby")
# elif(age<4):
#     print("toddler")
# elif(age<13):
#     print("kid")
# elif(age<20):
#     print("teenager")
# elif(age<65):
#     print("adult")
# elif(age>=65):
#     print("elder")

# favorite_fruits=["rambuttan","mangoostene","guava","water melon","mangoe"]


# fruit = "papaya"
# if fruit in favorite_fruits:
#     print(f"{fruit} is there")
# else:
#     print(f"{fruit} is not there")


# requested_toppings = ["cheese","sausage","peperoni"]
# for requested_topping in requested_toppings:
#     if requested_topping == "sausage":
#         print("sorry we are out of sausages")
#     else:
#         print(f"adding {requested_topping}")

# print("Your pizza is finished")

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
    
#     print("finished making your pizza")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print("finished making your pizza")