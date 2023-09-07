'''Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message'''
def show_messages(messages):
    for message in messages:
        print(message)

# Define a list of short text messages
messages = ["Hello!", "How are you?", "Python is fun!", "Goodbye!"]

# Call the function to display the messages
show_messages(messages)


'''Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly'''
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # Remove the first message from the list
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Define the list of short text messages
messages = ["Hello!", "How are you?", "Python is fun!", "Goodbye!"]

# Create an empty list to store sent messages
sent_messages = []

# Call the function to send and move messages
send_messages(messages, sent_messages)

# Print both lists to verify
print("Original messages:", messages)
print("Sent messages:", sent_messages)



'''Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages'''
# Define the list of short text messages
messages = ["Hello!", "How are you?", "Python is fun!", "Goodbye!"]

# Create an empty list to store sent messages
sent_messages = []

# Call the send_messages() function with a copy of the original list
send_messages(messages[:], sent_messages)

# Print both lists to show that the original list retains its messages
print("Original messages:", messages)
print("Sent messages:", sent_messages)
