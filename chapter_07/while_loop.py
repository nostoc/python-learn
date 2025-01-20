# current_number = 1
# while current_number<=5:
#     print(current_number)

#     current_number+=1

prompt = "\n Tell me some thing and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "


active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

