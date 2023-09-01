'''Consider a game featuring aliens that can have different colors and point
values. This simple dictionary stores information about a particular alien:'''

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary: -------------------------------------------
'''To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:'''

alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5} #dictionary has been defined
new_points = alien_0['points'] #pull the value associated with the key 'points' from the dictionary. value is then assigned to the variable new_points
print(f"You just earned {new_points} points!")

# Adding new key-value pairs:-----------------------------------------------------------
'''To add a new key-value pair, you would give the
name of the dictionary followed by the new key in square brackets, along
with the new value.

Let’s add two new pieces of information to the alien_0 dictionary: the
alien’s x- and y-coordinates, which will help us display the alien at a particular
position on the screen. Let’s place the alien on the left edge of the
screen, 25 pixels down from the top. Because screen coordinates usually
start at the upper-left corner of the screen, we’ll place the alien on the left
edge of the screen by setting the x-coordinate to 0 and 25 pixels from the
top by setting its y-coordinate to positive 25, as shown here:'''

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary---------------------------------------
'''define a dictionary with an empty set of braces and then add each key-value
pair on its own line'''

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# Modifying Values in a Dictionary:--------------------------------------------
'''To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with
that key'''
 
# consider an alien that changes from green to yellow as a game progresses:
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


'''let’s track the position of an alien that
can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien
should move:'''

# defining an alien with an initial x position and y position, and a speed of 'medium'
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 

# print the original value of x_position to see how far the alien moves to the right.
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
    y_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    y_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment
print(f"New position: {alien_0['x_position']} + {alien_0['y_position']}")

# Removing Key-Value Pairs------------------------------------------------------
# 1) using 'del' statement
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# A Dictionary of Similar Objects---------------------------------------------------
'''The previous example involved storing different kinds of information about
one object, an alien in a game. You can also use a dictionary to store one
kind of information about many objects. For example, say you want to poll a
number of people and ask them what their favorite programming language
is. A dictionary is useful for storing the results of a simple poll, like this:'''

# key is the name of a person who responded to the poll, and each value is their language choice
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using get() to Access Values------------------------------------------------------

'''
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

This results in a traceback, showing a KeyError:
Traceback (most recent call last):
File "alien_no_points.py", line 2, in <module>
print(alien_0['points'])
~~~~~~~^^^^^^^^^^
KeyError: 'points'
'''

# use the get() method to set a default value that will be returned if the requested key doesn’t exist
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)