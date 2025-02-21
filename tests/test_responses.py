import unittest
from bot.responses import get_response

class TestResponses(unittest.TestCase):
    def test_greeting_response(self):
        response = get_response("hello")
        self.assertIn(response, ["Hello!", "Hi there!", "Hey!"])

if __name__ == '__main__':
    unittest.main()