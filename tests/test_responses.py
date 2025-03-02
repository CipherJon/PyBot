import unittest
from bot.responses import get_response

class TestResponses(unittest.TestCase):
    def test_greeting_response(self):
        response = get_response("hello")
        self.assertEqual(response, "Hello! How can I assist you today?")

    def test_farewell_response(self):
        response = get_response("bye")
        self.assertEqual(response, "Goodbye! Have a wonderful day!")

    def test_unknown_response(self):
        response = get_response("unknown message")
        self.assertEqual(response, "I'm sorry, I don't understand.")

if __name__ == '__main__':
    unittest.main()