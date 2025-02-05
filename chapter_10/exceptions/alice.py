from pathlib import Path

path = Path("chapter_10/exceptions/alice.txt")


def count_words(path):
    """count the approximate number of words in the file"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass#print(f"Sorry the {path} file  does not exist.")
    else:

        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        # print(words)


file_names = [
    "chapter_10/exceptions/alice.txt",
    "chapter_10/exceptions/little_women.txt",
    "chapter_10/exceptions/sidhhartha.txt",
    "chapter_10/exceptions/moby_dick.txt",
]

for file_name in file_names:
    path = Path(file_name)
    count_words(path)
