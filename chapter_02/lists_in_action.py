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