'''Using a Function with a while Loop'''

# let’s use the get_formatted_name() function with a while loop to greet users more formally. Here’s a first attempt at greeting people using their first and last names:
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ").strip().lower()
    if f_name == 'q':
        break

    l_name = input("Last name: ").strip().lower()
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
