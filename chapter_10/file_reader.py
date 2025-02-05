from pathlib import Path

# path = Path("pi_million.txt")
# contents = path.read_text().rstrip()

# lines = contents.splitlines()

# pi_string = ""

# for line in lines:
#     pi_string = pi_string + line.strip()

# # print(f"{pi_string[:52]}")
# # print(len(pi_string))

# birthday=input("ENter your birthday in the form mmddyyyy : ")
# if birthday in pi_string:
#     print(f"Your birthday appears in first {len(pi_string)} digits of pi")
# else:
#     print(f"Your birthday doesnot appear in first {len(pi_string)} digits of pi")

"""Approach 01"""
path = Path("files-and-exceptions/learning_python.txt")
contents = path.read_text()
# print(contents)

"""Aprroach 2"""
# lines = contents.splitlines()
content_list =[]

for line in contents.splitlines():
    line = line.replace("Python", "C++")
    content_list.append(line)

# print(content_list)

for content_line in content_list:
    print(content_line)
