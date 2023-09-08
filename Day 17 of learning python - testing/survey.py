class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

            

'''This class starts with a survey question that you provide 1 and includes an empty list to store responses. 
The class has methods to print the survey question 2, add a new response to the response list 3, 
and print all the responses stored in the list 4. To create an instance from this class, all you have to provide is a question. 
Once you have an instance representing a particular
survey, you display the survey question with show_question(), store a
response using store_response(), and show results with show_results().
To show that the AnonymousSurvey class works, let’s write a program that
uses the class:'''