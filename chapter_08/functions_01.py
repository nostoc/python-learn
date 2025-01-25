def gree_user(username):
    """Display a simple greeting"""
    print(f"Hello {username.title()}")

gree_user("hansika")

def display_message(msg):
    print(f"{msg}")

display_message("I am learning about python functions is this chapter")

def favorite_book(title):
    print(f"My favorite book is {title.title()}")

favorite_book("Harry Potter Series")

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        print(f"{first_name} {middle_name} {last_name}")
    else:
        print(f"{first_name} {last_name}")

get_formatted_name("Hansika","Karunathilake")
get_formatted_name("Janitha","Karunarathna","Senani")

def build_person(first_name,last_name):
    person = { 'first' : first_name, 'last': last_name}
    return person

musician = build_person("John","Parker")
print(musician)

def make_shirt(size,msg):
    print(f"Your shirt is a {size} sized shirt with '{msg}' printed on it.")

make_shirt("L","I love cats")
make_shirt(msg="I love dos",size="M")

def build_musician(name,equipment,age=""):
    musician = {'name': name,'equipment':equipment, "age":age}

    return musician

janitha=build_musician(name="Janitha Senani",equipment="Guitar",age='23')
print(janitha)

while True:
    print("\nWhat is your full name? :")
    f_name = input("First Name : ")
    l_name = input("Last Name : ")

    formatted_name = get_formatted_name(f_name,l_name)
   
