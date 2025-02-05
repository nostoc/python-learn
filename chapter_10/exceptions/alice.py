from pathlib import Path

path = Path("chapter_10/exceptions/alice.txt")

def count_words(path):
    """count the approximate number of words in the file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry the {path} file  does not exist.")
    else:

        words  = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        # print(words)

