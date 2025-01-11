# aliens = []
# for alien_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)


# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["speed"] = "medium"
#         alien["points"] = 15
#     elif alien["color"] == "":
#         alien["color"] = "yellow"
#         alien["speed"] = "medium"
#         alien["points"] = 15

# for alien in aliens[:10]:
#     print(alien)


hansika = {"f_name": "hansika", "l_name": "karunathilake", "age": 23}
janitha = {"f_name": "janitha", "l_name": "karunarathna", "age": 23}
thilini = {"f_name": "thilini", "l_name": "subodahani", "age": 34}

people = [hansika, janitha, thilini]

for person in people:
    full_name = f"{person["f_name"].title()} {person["l_name"].title()}"
    age = person["age"]
    print(f"{full_name} is {age} years old.")
