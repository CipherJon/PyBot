import subprocess
import json

class Chatbot:
    def __init__(self, intents):
        self.intents = intents

    def get_response(self, message):
        intent = self.get_intent(message)
        if intent:
            # Call the JavaScript chatbot script
            process = subprocess.Popen(['node', 'js/chatbot.js'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=intent.encode())

            if stderr:
                raise Exception(f"Error in JS chatbot: {stderr.decode()}")

            return stdout.decode().strip()
        else:
            return "I'm sorry, I don't understand."

    def get_intent(self, message):
        for intent in self.intents:
            if intent['keyword'] in message.lower():
                return intent['name']
        return None