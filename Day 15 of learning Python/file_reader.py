"""Reading the Contents of a File"""

# program that opens pi_digits.txt , reads it, and prints the contents of the file to the screen
from pathlib import Path
path = Path('pi_digits.txt') # build a Path object representing the file pi_digits.txt, which we assign to the variable path
contents = path.read_text() # read_text() method to read the entire contents of the file
contents = contents.rstrip() # rstrip() method removes, or strips, any whitespace characters from the right side of a string
print(contents)

'''The only difference between this output and the original file is the
extra blank line at the end of the output. The blank line appears because
read_text() returns an empty string when it reaches the end of the file; this
empty string shows up as a blank line'''

'''strip the trailing newline character when we read the contents
of the file, by applying the rstrip() method immediately after calling
read_text(): contents = path.read_text().rstrip() : This approach is called method chaining'''

# Accessing a File’s Lines
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
  print(line)

# Working with a File’s Contents
'''to build a single string containing all the digits in the file with no
whitespace in it'''
'''start by reading the file and storing each line of digits in a list'''
pi_string = '' # create a variable, pi_string, to hold the digits of pi
for line in lines: # write a loop that adds each line of digits to pi_string
    pi_string += line.lstrip()
print(pi_string) # print this string
print(len(pi_string))

# Large Files: One Million Digits
from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi?
'''Let’s use the program we just wrote to find out if someone’s
birthday appears anywhere in the first million digits of pi. We can do this
by expressing each birthday as a string of digits and seeing if that string
appears anywhere in pi_string'''

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
   print("Your birthday appears in the first million digits of pi!")
else:
   print("Your birthday does not appear in the first million digits of pi.")