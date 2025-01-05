user_names= []
if user_names:
    for user_name in user_names:
        if user_name == "admin":
            print(f"Hello admin !, would you like to see a status report?")
        else:
            print(f"Helllo {user_name}, thank you for logging in again")
else:
    print("We need to find some users 😞")
    
current_usernames = ["janiya","Nostoc","cooper","ckekula","chutta"]
case_current_usernames=[]
for current_username in current_usernames:
    case_current_usernames.append(current_username.lower())
print(case_current_usernames)

new_usernams=["nostochk","cooperjsk","kekula","janiya","nostoc"]

for new_username in new_usernams:
    if new_username in case_current_usernames:
        print(f"The username {new_username} is already taken. Please try another one")
    else:
        print(f"The {new_username} is avaible, you can use it.")
        
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print("1st")
    if number == 2:
        print("2nd")
    if number == 3:
        print("3rd")
    else:
        print(f"{number}th")
