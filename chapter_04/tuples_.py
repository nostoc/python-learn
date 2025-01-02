# tuple = immutable list
#tuple =("a","b")
# ( ) are used instead of [ ]
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 233

foods = ("rice","dhal","fish","papdam","mallum","soya meat")
for food in foods:
    print(food)
# foods[2]= "mango curry" cant modify
#but can reassign bew values
print("\n")
foods = ("rice","dhal","fish","papdam","mallum","soya meat","mangoe curry")
for food in foods:
    print(food)
