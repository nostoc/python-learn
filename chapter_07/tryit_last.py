sandwich_orders =[  'tuna', 'chicken', 'pastrami', 'beef']
finished_sandwiches=[]

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)
    
print("\n----List of Finished Sandwiches----\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich\n")
