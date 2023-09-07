'''Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza,
instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!'''

# List of favorite pizza kinds
favorite_pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

# Print pizza names using a for loop
print("My favorite pizzas:")
for pizza in favorite_pizzas:
    print(pizza)

# Print sentences about each pizza
print("\nI like these pizzas:")
for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")

# Print an additional sentence about loving pizza
print("\nI really love pizza!")
