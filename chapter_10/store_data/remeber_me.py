from pathlib import Path
import json

username = input("What is your user name? ")
path = Path("chapter_10/store_data/username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you when you come back {username}")