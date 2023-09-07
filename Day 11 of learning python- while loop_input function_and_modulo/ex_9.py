'''Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll'''

# Dream Vacation: Poll users about their dream vacation.
poll_results = []
while True:
    response = input("If you could visit one place in the world, where would you go? (Enter 'quit' to end the poll): ")
    if response.lower() == 'quit':
        break
    poll_results.append(response)

# Print the results of the poll.
print("\nPoll Results - Dream Vacation Destinations:")
for idx, destination in enumerate(poll_results, start=1):
    print(f"{idx}. {destination}")
