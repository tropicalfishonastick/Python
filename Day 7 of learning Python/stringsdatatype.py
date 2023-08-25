#---------------------------------------------------------STRINGS--------------------------------------------------------#

"This is a string."
'This is also a string.'
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using Variables in Strings
# f-strings - The f is for format, because Python
# formats the string by replacing the name of any variable in braces with its
# value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines
# To add a tab to your text, use the character combination \t:
print("Python")
print("\tPython")

# To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")

# combine tabs and newlines in a single string
# The string "\n\t" tells Python to move to a new line, and start the next line with a tab.
# The following example shows how you can use a one-line string to generate four lines of output
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# compare two strings to determine whether they are the same
string1 = "hello"
string2 = "world"

if string1 == string2:
    print("The strings are the same.")
else:
    print("The strings are different.")

# Python can look for extra whitespace on the right and left sides of a
# string. To ensure that no whitespace exists at the right side of a string, use
# the rstrip() method:
favorite_language = 'python '
print(favorite_language.rstrip())

favorite_language = favorite_language.rstrip()
print(favorite_language)

# removing extra white spaces from left side - lstrip() method
favorite_lang = ' python'
favorite_lang = favorite_lang.lstrip()
print(favorite_lang)

# removing extra whitespaces from both sides - strip() method
fav_lang = ' PYTHON '
fav_lang = fav_lang.strip()
print(fav_lang)

# Removing Prefixes - startswith() method and string slicing
nostarch_url = 'https://nostarch.com' # nostarch_url is a variable that holds the string 'https://nostarch.com'

# Check if the string starts with the prefix 'https://' - startswith() method
if nostarch_url.startswith('https://'):
    # Remove the prefix using string slicing
    nostarch_url = nostarch_url[len('https://'):] 
    # len('https://') calculates the length of the prefix 'https://', which is 8 characters.
    # nostarch_url[len('https://'): ] uses string slicing to create a new string starting from the character after the 8th character (which is the first character after the prefix 'https://'). The colon (:) indicates slicing, and leaving the second part of the slice empty means "up to the end of the string."
    # So, when you execute the line of code:
    # The slicing extracts the part of the nostarch_url string starting from the 9th character (after removing the prefix 'https://'), and continues until the end of the string.
    # This extracted portion is assigned back to the nostarch_url variable, effectively removing the prefix 'https://'

print(nostarch_url)

# alternate way - removeprefix() method
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)


# Avoiding Syntax Errors with Strings
# apostrophe error within single quotes
# The apostrophe appears inside a set of double quotes, so the Python
# interpreter has no trouble reading the string correctly
message = "One of Python's strengths is its diverse community."
print(message)

# if you use single quotes, Python can’t identify where the string should end
#  message = 'One of Python's strengths is its diverse community.'
# SyntaxError: unterminated string literal (detected at line 103)
'''message = 'One of Python's strengths is its diverse community.'
print(message)'''

# ----------------------------------------------------------------------------------------------------

