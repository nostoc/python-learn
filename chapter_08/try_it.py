def show_messages(message_list):
    for mesage in message_list:
        print(mesage)

def send_messages(message_list,sent_messges):
    while message_list:
        for message in message_list:
            current_message = message_list.pop()
            sent_messges.append(current_message)
    



text_messages = ["message 01","message 02","message 03","message 04","message 05","message 06"]
sent_messges=[]

show_messages(text_messages)
send_messages(text_messages[:],sent_messges)
print(text_messages)
print(sent_messges)



