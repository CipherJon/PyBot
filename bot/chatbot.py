from loguru import logger
from bot.responses import get_response

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.setup_logging()
    
    def setup_logging(self):
        logger.add("logs/bot.log", rotation="1 MB")
    
    def start(self):
        print(f"Hello! I am {self.name}. How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Goodbye!")
                break
            response = get_response(user_input)
            print(f"{self.name}: {response}")
            logger.info(f"User: {user_input} | Bot: {response}")