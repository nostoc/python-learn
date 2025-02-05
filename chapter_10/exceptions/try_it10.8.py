from pathlib import Path

dogs_path = Path("chapter_10/exceptions/dogs.txt")
cats_path = Path("chapter_10/exceptions/cats.txt")

def read_file(path):
    contents = dogs_path.read_text()
    print(f"COntents of the file {path}")
    print(contents)

read_file(cats_path)
read_file(dogs_path)
