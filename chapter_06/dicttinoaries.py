hansika = {"f_name": "hansika", "l_name":"karunathilake","age":23,"city":"Gampaha",}
print(f"{hansika["f_name"].title()} {hansika['l_name'].title()} is {hansika['age']} years old. She is from {hansika['city']}")

fav_numbers= {"hansi":5,"jani":3,"kavi":1,"seww":4,"thilini":8}
print(f"Hansi's favorite number is : {fav_numbers["hansi"]}")
print(f"Jani's favorite number is : {fav_numbers["jani"]}")
print(f"Kavi's favorite number is : {fav_numbers["kavi"]}")
print(f"seww's favorite number is : {fav_numbers["seww"]}")
print(f"thilini's favorite number is : {fav_numbers["thilini"]}")

user_0 = {
    "username":"Nostoc",
    "first":"Hansika",
    "last":"karunathilake",
}

for key, value in user_0.items():
    print(f"\nKey : {key}")
    print(f"Value : {value}\n")


for value in hansika.values():
    print(value)
    