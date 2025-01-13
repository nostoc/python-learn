import os

os.system("cls")

# # name = input("Please enter your name: ")
# # print(f"\nHello, {name}")

# prompt = "If you share your name, we will able to give a personalized greeting. "
# prompt += "So what is your name? :"
# name = input(prompt)
# print(name)

# age = input("How old are you? \t:")
# age = int(age)
# print(age>=18)

# car = input("What type of car are you looking for? :")
# print(f"Let me see if I can find you a {car}")

# number_of_visitors = input("How many visitors do you expect? : ")
# number_of_visitors = int(number_of_visitors)
# if number_of_visitors > 8:
#     print("You will have to wait for a table")
# else:
#     print("Your table is ready")

# number = input("ENter a number you wish... ")
# number = int(number)
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10")
# else:
#     print(f"{number} is not divisible by 10.")

# prompt = "Please enter the name of city you have visited"
# prompt += "\nENter 'quit' to end.\n:"

# while True:
#     city=input(prompt)
#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
#     print(current_num)

# prompt = "ENTER THE TOPPING YOU WANT."
# prompt += "\nto end type 'q'"
# prompt += "\nMy answer : "
# active = True

# while active:
   
#     topping = input(prompt)
#     if topping == "q":
#         print("Exiting programm..")
#         active = False
#     else:
#         print(f"\n{topping.title()} is adding to your pizaa...\n")

prompt = "Enter your age : "

active = True


while active:
    
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("You have a free ticket casue you are a toddler. \n Enjoy the show kiddo..!")
        active = False
        
    elif age <= 12:
        print("You will be charged $10 for the movie. Enjoy the show...")
        active =False
        
    else:
        print("Your ticket is $12. Enjoy the show...")
        active = False

        