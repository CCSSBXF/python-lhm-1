import unittest
from Nov_7_1 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'what language did you learn first'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'spanish', 'chinese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
# 单个的测不出来，多个的可以，原因未知
    def test_story_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


if __name__=='__main__':
    unittest.main()