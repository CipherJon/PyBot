import json

def load_intents():
    with open('data/intents.json') as f:
        return json.load(f)

def get_response(user_input):
    if user_input.lower() == "goodbye":
        close_program()
    intents = load_intents()
    for intent in intents:
        if intent['keyword'] in user_input.lower():
            return generate_response(intent['name'])
    return "I'm sorry, I don't understand."

def close_program():
    print("Goodbye! Have a great day!")
    exit()

def generate_response(intent_name):
    responses = {
        "greeting": "Hello! How can I assist you today?",
        "farewell": "Goodbye! Have a wonderful day!",
        # Add more responses as needed
    }
    return responses.get(intent_name, "I'm sorry, I don't understand.")