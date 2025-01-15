uncornfirmed_users = ["ashani","janani","hansika"]
confirmed_users = []
while uncornfirmed_users:
    current_user = uncornfirmed_users.pop()
    print(f"Verifying user : {current_user.title()}")
    confirmed_users.append(current_user)

print("\nList of verified users\n")
for user in confirmed_users:
    print(user.title())
print(uncornfirmed_users)