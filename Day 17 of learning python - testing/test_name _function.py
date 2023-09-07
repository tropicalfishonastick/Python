# A Passing Test
'''write a single test function. The test function will call the function we’re testing, 
and we’ll make an assertion about the value that’s returned. If our assertion is correct, the test will pass; 
if the assertion is incorrect, the test
will fail.'''

# Here’s the first test of the function get_formatted_name():
from name import get_formatted_name
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


"""
1. The name of a test file is important; it must start with test_. When we ask pytest
to run the tests we’ve written, it will look for any file that begins with test_,
and run all of the tests it finds in that file.

2. In the test file, we first import the function that we want to test: get
_formatted_name(). Then we define a test function: in this case, test_first
_last_name()

3. test names should be longer and more descriptive than a typical
function name

4. You’ll never call the function yourself; pytest will find the
function and run it for you

5. An assertion is a claim about a condition.
Here we’re claiming that the value of formatted_name should be 'Janis
Joplin'.

6. If you run the file test_name_function.py directly, you won’t get any output
because we never called the test function. Instead, we’ll have pytest run the
test file for us.
"""