class AnonymousSurvey():
    """Collect anonymous answers to the questions in a survey."""

    def __init__(self, question):
        """Stores question and prepare to store answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Shows question from survey."""
        print(self.question)

    def store_response(self, new_response):
        """Stores single answer to question from survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Shows all answers from survey."""
        print('The results of the survey:')
        for response in self.responses:
            print(f'- {response}')