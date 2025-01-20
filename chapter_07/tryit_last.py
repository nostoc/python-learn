sandwich_orders =[  'pastrami','tuna','pastrami', 'chicken', 'pastrami', 'beef','pastrami',]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches=[]

while sandwich_orders:
    for sandwich in sandwich_orders:
        if sandwich=='pastrami':
            sandwich_orders.remove(sandwich)     
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)
    
print("\n----List of Finished Sandwiches----\n")
print(f"\nDeli has run out of pastrami\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich\n")
