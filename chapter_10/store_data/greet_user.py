from pathlib import Path
import json

path = Path("chapter_10/store_data/username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome Back {username}")
