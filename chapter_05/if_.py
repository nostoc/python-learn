cars = ["audi","bmw","ferrari","bugati"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "maruti"
print("Is Car == 'Maruti'? I predict true")
print(car =="maruti")

banned_users = ["janitha","chamuditha","dhanuja"]
user_ = "irushi"
if user_ in banned_users:
    print(f"{user_}, you are banned.")
else:
    print(f"{user_}, you are a good user.")
    
    

age = 22
if age>23 or age<=30:
    print("Authorized")
else:
    print("Unauthorized")
    
age = 12
if age<4:
    print("$4")
elif age <18:
    print("$25")
else:
    print("$40")