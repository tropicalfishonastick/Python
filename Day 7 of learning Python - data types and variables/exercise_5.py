# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
# Store names of friends in a list called names
names = ["Alice", "Bob", "Charlie", "David"]

# Print each person's name by accessing each element in the list
for name in names:
    print(name)



# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.
# Store names of friends in a list called names
names = ["Alice", "Bob", "Charlie", "David"]

# Print a personalized message to each person
message = "Hello, {}! How are you doing today?"
# In this line, a string variable named message is assigned the value "Hello, {}! How are you doing today?". This string contains a pair of curly braces {} as a placeholder for where the name will be inserted

for name in names:
    print(message.format(name))
# n this block of code, you're using a loop to iterate through each name in the names list. For each name in the list:
# name is a variable that holds the current name being processed in the loop.
# message.format(name) replaces the curly braces {} in the message string with the value of the name variable. This effectively substitutes the placeholder in the message with the current name.
#print(...) prints the formatted message to the console.
#So, for each name in the names list, the program formats the message by inserting the current name into the placeholder and then prints the personalized message


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
# Store examples of favorite modes of transportation in a list
transportation = ["motorcycle", "car", "bicycle", "scooter"]

# Print statements about each item in the list
for item in transportation:
    print("I would like to own a", item)
