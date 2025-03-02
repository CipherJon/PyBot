import json
from bot.chatbot import Chatbot
from config import settings

with open('data/intents.json') as f:
    intents = json.load(f)

chatbot = Chatbot(intents)

print(f"{settings.BOT_NAME} is now running...")

while True:
    message = input("You: ")
    response = chatbot.get_response(message)
    print(f"Bot: {response}")