import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the AnonymousSurvey class."""

    def setUp(self):
        """Create a survey and reponses to use in all tests methods."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'spanish', 'polish']

    def test_store_single_response(self):
        """Check that the single response is stored valid."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses[0])

    def test_store_three_response(self):
        """Check that the three single responses are stored valid."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
