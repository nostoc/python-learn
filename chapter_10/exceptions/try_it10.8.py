from pathlib import Path

dogs_path = Path("chapter_10/exceptions/dogs.txt")
cats_path = Path("chapter_10/exceptions/cats.txt")

def read_file(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass# print(f"Oops the {path} file doesnot exist.")
    else:
        print(f"Contents of the file {path}")
        print(contents)

read_file(cats_path)
read_file(dogs_path)
