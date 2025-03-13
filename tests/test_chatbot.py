import unittest
from bot.chatbot import Chatbot
import json

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_greeting(self):
        response = self.chatbot.get_response('hello')
        self.assertEqual(response, "Hello! How can I assist you today?")

    def test_farewell(self):
        response = self.chatbot.get_response('bye')
        self.assertEqual(response, "Goodbye! Have a wonderful day!")

    def test_unknown_intent(self):
        response = self.chatbot.get_response('unknown message')
        self.assertEqual(response, "I'm sorry, I don't understand.")

if __name__ == '__main__':
    unittest.main()