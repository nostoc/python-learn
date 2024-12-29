bicycles =["hyundai", "hudson", "DSI", "Tomahwak"]
print(bicycles)
print(bicycles[0].title())
#last item : [-1]
print(bicycles[-1])

names = ["Janitha","Marlin","Sewwandi"]
print(names[0])
print(names[1])
print(names[2])
print(f"Hello there, {names[0]}")
print(f"Hello there, {names[1]}")
print(f"Hello there, {names[2]}")

names.append("Dhanuja")
print(names)
names.insert(1,"Dhathiya")
print(names)
del names[3]
print(names)

poped_name = names.pop()
print(poped_name)

pooped_name = names.pop(0)
print(pooped_name)

names.remove("Marlin")
print(names)

people = ["janitha","amma","thaththa","Suddi akka","marlin","loku akka"]

print(f"Hey {people[0]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[1]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[2]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[3]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[4]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[5]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")

print(f"{people[4]} said she won't come.")

people.insert(4,"Senani")

print(f"Hey {people[0]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[1]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[2]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[3]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[4]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[5]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")

print("Hey people, I found a bigger table. SO I am gonna invite three more friends.")

people.insert(0,"Chooty Akka")
people.insert(3,"Sameera")
people.append("Ashani")

print(f"Hey {people[0]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[1]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[2]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[3]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[4]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[5]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[6]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[7]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[8]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")
print(f"Hey {people[9]}, there is a dinner party at my place tommorow night. Your participation is much appreciated. ")


print("Oh I am so sorry people, I won't be getting that new table. So I can invite only two people.")
removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please Don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

removed_person = people.pop()
print(f"I am so sorry for your inconvienience {removed_person}.Please don't come to my dinner party. ")
print(people)

print(f"\n{people[0]} you are still invited")
print(f"{people[1]} you are still invited")

del people[0]
del people[0]

print("\n")
print(people)
