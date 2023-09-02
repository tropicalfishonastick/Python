'''Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''

while True:
    age = input("Enter your age (type 'quit' to finish): ")

    if age == 'quit':
        break  # Exit the loop if the user enters 'quit'

    age = int(age)  # Convert the input to an integer

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
