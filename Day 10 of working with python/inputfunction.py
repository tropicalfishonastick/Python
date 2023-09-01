'''-----------------------------------------How the input() Function Works-----------------------------------------'''

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

'''-----------------------------------------Writing Clear Prompts--------------------------------------------------'''
name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# to build a multiline string
# first line assigns the first part of the message to the variable prompt
prompt = "If you share your name, we can personalize the messages you see."
# the operator += takes the string that was assigned to prompt and adds the new string onto the end.
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

'''----------------------------------Using int() to Accept Numerical Input-----------------------------------------------'''
age = input("How old are you? ")
print(age)
print(type(age))
# here age is not an integer but a string

age = int(input("How old are you?"))
print(age)
print(type(age))
# here age is an integer not a string

# another example
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
   print("\nYou're tall enough to ride!")
else:
   print("\nYou'll be able to ride when you're a little older.")
