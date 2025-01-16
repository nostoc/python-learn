# uncornfirmed_users = ["ashani","janani","hansika"]
# confirmed_users = []
# while uncornfirmed_users:
#     current_user = uncornfirmed_users.pop()
#     print(f"Verifying user : {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nList of verified users\n")
# for user in confirmed_users:
#     print(user.title())
# print(uncornfirmed_users)

# pets =["cat","dog","parrot","fish","cat","duck","cat"]

# while 'cat' in pets:
#     pets.remove('cat')

# for pet in pets:
#     print(pet)

reponses = {}
polling_active = True # flag

while polling_active:
    name = input("\nWhat is your name ? ")
    reponse = input("\nWhich mountain would you like to climb someday ? ")
    reponses[name] = reponse
    repeat = input("Would you like to let another person repond ? (yes/no) \n\t:")
    if repeat == 'no':
        polling_active = False

print("\n-------POLLING RESULTS-------")
for name, reponse in reponses.items():
    print(f"{name.title() } would like to climb {reponse.title()} mountain one day.")
print("\n")

