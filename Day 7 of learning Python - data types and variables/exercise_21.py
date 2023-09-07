'''More Loops: All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Adding a new food to my_foods
my_foods.append('sushi')

# Adding a different food to friend_foods
friend_foods.append('ice cream')

# Print my favorite foods using a for loop
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Print friend's favorite foods using a for loop
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
