from pathlib import Path
import json

def get_stored_name(path):
    '''Get user name if available'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    


def greet_user():
    """Greet the user by name"""
    path = Path("chapter_10/store_data/username.json")
    username = get_stored_name(path)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = input("What is your user name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you come back {username}")

greet_user()
