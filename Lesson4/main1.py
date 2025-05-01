from pathlib import Path
import json

song = {}

song["Artist"] = "Michael Jackson"
song["Title"] = "Billie jean"
song["Release Year"] = "1983"
song["Modern"] = False

print(song)

path = Path("Lesson4/song.json")
contents = json.dumps(song)
path.write_text(contents)
print(contents)

contents = path.read_text()
song = json.loads(contents)
print(song)