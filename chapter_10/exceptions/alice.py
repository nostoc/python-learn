from pathlib import Path

path = Path("chapter_10/exceptions/alice.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Sorry the file 'alice.txt' does not exist")
else:
    #count the number of words in the file
    words  = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    #print(words)
