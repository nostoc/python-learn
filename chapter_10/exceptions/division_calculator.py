# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero !")


print("Give me two numbers and I'll divide them")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number.lower() == "q":
        break
    second_number = input("\nSecond Number: ")
    if second_number.lower() == "q":
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Your answer is : {answer}")
    
