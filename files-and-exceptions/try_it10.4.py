from pathlib import Path

# path = Path("files-and-exceptions/guests.txt")
path = Path("files-and-exceptions/guest_book.txt")

# path.write_text(name)

guest_book =[]
content= ''


while True:
    name = input("Enter your name ? (enter 'q' to exit.)")
    
    if name =='q':
        break
    guest_book.append(name)

for guest in guest_book:
    content += f'{guest}\n'

path.write_text(content)
