# def make_pizza(*toppings):
#     print("\n...Making a pizza with the following toppings...")
#     for topping in toppings:
#         print(f"\t-{topping}")
    
# # make_pizza("pepparoni")
# make_pizza("cheese","sausage")

# def make_pizza_with_size(size,*toppings):
#     print(f"\n...Making a {size} sized pizza with the following toppings...")
#     for topping in toppings:
#         print(f"\t-{topping}")


# make_pizza_with_size("Medium","cheese","sausage","pepparoni","chicken","beef")

def build_profile(first_name, last_name,**user_info):
    user_info["first_name"]=first_name
    user_info["last_name"]=last_name
    return user_info

hansika_profile = build_profile("hansika","Karunathilake",age=23,city="Gampha",boy_friend="Janitha Senani")
print(hansika_profile)