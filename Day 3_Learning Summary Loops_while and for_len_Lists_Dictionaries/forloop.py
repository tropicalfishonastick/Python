# Loop using explicit values in the list [0, 1, 2]
for i in [0, 1, 2]:
    # Print "meow" for each value of 'i'
    print("meow")

# Loop using the range function with a stop value of 3
for i in range(3):
    # Print "meow" for each value of 'i' (0, 1, 2)
    print("meow")

# Loop using the range function with a stop value of 3, but ignoring the loop variable with '_'
for _ in range(3):
    # Print "meow" three times (no use of loop variable)
    print("meow")

# Print the string "meow" repeated three times using the string repetition operator '*'
print("meow" * 3)

# Print the string "meow" followed by a newline character, repeated three times using string repetition and 'end=""'
print("meow\n" * 3, end="")
