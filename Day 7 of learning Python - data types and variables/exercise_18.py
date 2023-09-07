# List Comprehension 
'''Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.'''

for i in range(1, 21):
    print(i)

#-------------------------------------------------------------------------------------------

'''One Hundred: Make a list of the numbers from one to one hundred, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.'''

numbers = list(range(1, 101))

for number in numbers:
    print(number)

#-------------------------------------------------------------------------------------------

'''Summing a Hundred: Make a list of the numbers from one to one hundred, and
then use min() and max() to make sure your list actually starts at one and ends
at one hundred. Also, use the sum() function to see how quickly Python can add
a hundred numbers.'''

numbers = list(range(1, 101))

minimum = min(numbers)
maximum = max(numbers)
sum_of_numbers = sum(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", sum_of_numbers)

#---------------------------------------------------------------------------------------

'''Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.'''

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

#---------------------------------------------------------------------------------------

'''Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list.'''

multiples_of_three = list(range(3, 31, 3))

for number in multiples_of_three:
    print(number)

#----------------------------------------------------------------------------------------

'''Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.'''

cubes = [num ** 3 for num in range(1, 11)]
print(cubes)
#-----------------------------------------------------------------------------------------

'''Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes.'''

cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

