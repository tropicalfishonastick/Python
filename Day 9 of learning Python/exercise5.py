'''Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''

# Example conditional tests

# Test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # Predicts True because 'car' is indeed equal to 'subaru'

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # Predicts False because 'car' is not equal to 'audi'

# Test 3
number = 10
print("\nIs number > 5? I predict True.")
print(number > 5)  # Predicts True because 10 is greater than 5

# Test 4
print("\nIs number < 0? I predict False.")
print(number < 0)  # Predicts False because 10 is not less than 0

# Test 5
name = 'Alice'
print("\nIs name == 'alice'? I predict False.")
print(name == 'alice')  # Predicts False because 'name' is not equal to 'alice'

# Test 6
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # Predicts True because 'name' when lowercased is 'alice'

# Test 7
temperature = 78
print("\nIs temperature >= 70 and temperature <= 80? I predict True.")
print(temperature >= 70 and temperature <= 80)  # Predicts True because 78 falls within the range

# Test 8
print("\nIs temperature > 80 or temperature < 60? I predict False.")
print(temperature > 80 or temperature < 60)  # Predicts False because 78 is not greater than 80 and not less than 60

# Test 9
has_car = True
print("\nDoes the person have a car? I predict True.")
print(has_car)  # Predicts True because 'has_car' is True

# Test 10
is_student = False
print("\nIs the person a student? I predict False.")
print(is_student)  # Predicts False because 'is_student' is False
