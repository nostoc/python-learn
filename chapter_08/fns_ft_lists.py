# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)

# usernames= ["Hannah","Abbot","Ty","MAgret"]
# greet_users(usernames)

def print_models(unprinted_models,printed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"printing {current_model}...")
        printed_models.append(current_model)

def show_printed_models(printed_models):
        for model in printed_models:
            print(f"{model} is finished...")


unprinted_models = ["3D car", "Tetrahedron","robot pendant","car sheild"]
printed_models = []
print_models(unprinted_models[:],printed_models)
show_printed_models(printed_models)
print("\n")
print(unprinted_models)