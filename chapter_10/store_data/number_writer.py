from pathlib import Path
import json

numbers = [2,4,5,6,7,22,23,5,]

path = Path("chapter_10/store_data/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
