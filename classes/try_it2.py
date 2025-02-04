class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print(f"First name : {self.first_name}\nLast name : {self.last_name}")
        print("\nOther information of user")
        print(f"{self.user_info}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")

class Priveleges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can add user"]

    def show_priveleges(self):

        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.priveleges = Priveleges()


admin = Admin("Janitha","Senai",age=23,home_location="Kelaniya")
admin.priveleges.show_priveleges()
