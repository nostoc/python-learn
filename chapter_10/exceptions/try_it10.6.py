print("Give me two numbers and I'll add them")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number.lower() == "q":
        break
    second_number = input("\nSecond Number: ")
    if second_number.lower() == "q":
        break
    try:
       answer = int(first_number) + int(second_number)
    except ValueError:
       print("You can't add numbers with literlas! \n Please enter numbers only.")
    else:
       print(f"Your answer is : {answer}")
