magicians = ["Alice","harry Potter","Merlin", "Tom Riddle","Albus Dumboldore"]
for magician in magicians:
    print(magician)

message = "Hi"
print(message)

fav_pizzas = ["Chicken & cheese","peperoni","chicken bomb","meat & sausage"]
for pizza in fav_pizzas:
    print(f"I like {pizza} pizza.")
print("\nI like to eat pizza sooooooooooooooooo much.")
print("I really love pizza.\n")

animals = ["cat","dog","panther"]
for animal in animals:
    print(f"A {animal} is a mammal.")
print("Any of these animals is a mamal.")

freind_pizza = fav_pizzas[:]
print(freind_pizza)
fav_pizzas.append("burger pizza")
freind_pizza.append("kottu pizza")
print(f"my favorite pizzas are : \t")
for pizza in fav_pizzas:
    print(pizza)
print(f"freind's favorite pizzas are : {freind_pizza[:]}")




