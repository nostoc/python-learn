from pathlib import Path

path = Path("pi_million.txt")
contents = path.read_text().rstrip()

lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string = pi_string + line.strip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))

birthday=input("ENter your birthday in the form mmddyyyy : ")
if birthday in pi_string:
    print(f"Your birthday appears in first {len(pi_string)} digits of pi")
else:
    print(f"Your birthday doesnot appear in first {len(pi_string)} digits of pi")