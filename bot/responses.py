import json
import random
import nltk

nltk.download('punkt')

def load_intents():
    with open('data/intents.json', 'r') as file:
        intents = json.load(file)
    return intents

def get_response(user_input):
    intents = load_intents()
    for intent in intents['intents']:
        if user_input.lower() in intent['patterns']:
            return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that."