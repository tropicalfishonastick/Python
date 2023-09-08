import pytest

from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

    ''' create an instance called language_survey To test the behavior of a class, we need to make an instance of the class. We create an instance called language_survey 2 with the question
"What language did you first learn to speak?" We store a single response, English, using the store_response() method. Then we verify that the response was stored correctly by asserting that English is in the list language_survey
.responses 3.'''

# Let’s verify that three responses can be stored correctly. To do this, we add another method to TestAnonymousSurvey:
def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses

        '''We call the new function test_store_three_responses(). We create a survey
object just like we did in test_store_single_response(). We define a list
containing three different responses 1, and then we call store_response()
for each of these responses. Once the responses have been stored, we
write another loop and assert that each response is now in language_survey
.responses 2.
When we run the test file again, both tests (for a single response and
for three responses) pass:'''

'''We need to import pytest now, because we’re using a decorator that’s defined in pytest. 
We apply the @pytest.fixture decorator 1 to the new function language_survey() 2. 
This function builds an AnonymousSurvey object and returns the new survey.
Notice that the definitions of both test functions have changed 3 5; each test function now has a parameter called language_survey. When
a parameter in a test function matches the name of a function with the
@pytest.fixture decorator, the fixture will be run automatically and
the return value will be passed to the test function. In this example, 
the function language_survey() supplies both test_store_single_response() and test_store_three_responses() with a language_survey instance.
There’s no new code in either of the test functions, but notice that two lines have been removed from each function 4 6: 
the line that defined a question and the line that created an AnonymousSurvey object.
When we run the test file again, both tests still pass. These tests would be particularly useful when trying to expand AnonymousSurvey to 
handle multiple responses for each person. After modifying the code to accept multiple responses, you could run these tests and make sure you haven’t affected the ability to store a single response or a series of individual responses.'''
