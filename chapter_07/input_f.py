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

car = input("What type of car are you looking for? :")
print(f"Let me see if I can find you a {car}")

number_of_visitors = input("How many visitors do you expect? : ")
number_of_visitors = int(number_of_visitors)
if number_of_visitors > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")

number = input("ENter a number you wish... ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not divisible by 10.")
