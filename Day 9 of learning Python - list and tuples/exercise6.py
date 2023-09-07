'''More Conditional Tests: You don’t have to limit the number of tests you create
to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

# Conditional Tests

# Tests for equality and inequality with strings
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

# Tests using the lower() method
name = 'John'
print("\nIs name.lower() == 'john'? I predict True.")
print(name.lower() == 'john')

print("\nIs name.lower() == 'mary'? I predict False.")
print(name.lower() == 'mary')

# Numerical tests
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age > 30? I predict False.")
print(age > 30)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 20? I predict True.")
print(age >= 20)

print("\nIs age <= 30? I predict True.")
print(age <= 30)

# Tests using the and and or keywords
temperature = 85
time_of_day = 'afternoon'
print("\nIs temperature > 80 and time_of_day == 'afternoon'? I predict True.")
print(temperature > 80 and time_of_day == 'afternoon')

print("\nIs temperature > 90 or time_of_day == 'morning'? I predict True.")
print(temperature > 90 or time_of_day == 'morning')

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print('grape' in fruits)

# Test whether an item is not in a list
vegetables = ['carrot', 'broccoli', 'spinach']
print("\nIs 'zucchini' not in vegetables? I predict True.")
print('zucchini' not in vegetables)

print("\nIs 'carrot' not in vegetables? I predict False.")
print('carrot' not in vegetables)
