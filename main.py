from bot.chatbot import ChatBot
from config.settings import BOT_NAME

def main():
    bot = ChatBot(BOT_NAME)
    bot.start()

if __name__ == "__main__":
    main()