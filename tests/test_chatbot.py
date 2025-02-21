import unittest
from bot.chatbot import ChatBot

class TestChatBot(unittest.TestCase):
    def test_initialization(self):
        bot = ChatBot("TestBot")
        self.assertEqual(bot.name, "TestBot")

if __name__ == '__main__':
    unittest.main()