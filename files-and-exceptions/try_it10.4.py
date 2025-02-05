from pathlib import Path

path = Path("files-and-exceptions/guests.txt")
name = input("What is your name ?")
path.write_text(name)
