from pathlib import Path
import json


def greet_user():
    """Greet the user by name"""
    path = Path("chapter_10/store_data/username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome Back {username}!")
    else:
        username = input("What is your user name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you come back {username}")

greet_user()