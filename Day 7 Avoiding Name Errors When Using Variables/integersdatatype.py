# NUMBERS :---------------------------------------------------------------------------
# 1) INTEGERS
print(2 + 3) # add

print(3 - 2) # subtract

print(2 * 3) # multiply

print(3 / 2) # divide

print(3**2) # exponent(two multiplication symbols to represent exponents) - 3 to the power 2

print(10000**5) # exponent

print(2 + 3*4) # Python supports the order of operations too

# 2) FLOAT - Python calls any number with a decimal point a float
print(0.1 + 0.1)

print(4/2) # When you divide any two numbers, even if they are integers that result in a
#whole number, you’ll always get a float

print(1 + 2.0) # mix an integer and a float in any other operation, you’ll get a float as well

# Underscores in Numbers ----------------------------------------------------------------------------
# When you’re writing long numbers, you can group digits using underscores to make large numbers more readable
universe_age = 14_000_000_000

# When you print a number that was defined using underscores, Python prints only the digits. This
# feature works for both integers and floats
print(universe_age)

# Multiple Assignment -------------------------------------------------
x, y, z = 1, 2, 3
