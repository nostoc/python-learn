from pathlib import Path

contents = "I lve cats\n"
contents += 'I love programming\n'
contents += 'I love Machine Learning'


path = Path("files-and-exceptions/programming.txt")
path.write_text(contents)
