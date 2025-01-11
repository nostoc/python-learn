aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)


for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 15
    elif alien["color"] == "":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 15

for alien in aliens[:10]:
    print(alien)
