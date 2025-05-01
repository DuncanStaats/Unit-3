from pathlib import Path
import json

user_name = input("What is your name: ")

# Stores user's name in json file
path = Path("Lesson4/username.json")
contents = json.dumps(user_name)
path.write_text(contents)

# Retrieves user's name from json file
contents = path.read_text()
user_name2 = json.loads(contents)
print(f"Welcome back {user_name2}!")
