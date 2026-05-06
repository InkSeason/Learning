message = ["Hello, world!", "Welcome to Python programming.",
            "Have a great day!"]
sent_message = []

def show_message(msg):
    # print(f"showing {msg}:")
    for m in msg:
        print(m)

show_message(message)

def send_message(message, sent_message):
    while message:
        current_message = message.pop(0)
        print(f"Sending message: {current_message}")
        sent_message.append(current_message)

send_message(message[:], sent_message)

show_message(sent_message)
show_message(message)

