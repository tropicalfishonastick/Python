'''Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza'''

# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Use a while loop to keep prompting the user for toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping == 'quit':
        break  # Exit the loop if the user enters 'quit'
    else:
        print(f"Adding {topping} to your pizza.")
        pizza_toppings.append(topping)

# Display the list of chosen pizza toppings
print("Your pizza will have the following toppings:")
for topping in pizza_toppings:
    print(topping)
