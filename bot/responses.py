import json

def load_intents():
    with open('data/intents.json') as f:
        return json.load(f)

def get_response(user_input):
    if user_input.lower() == "goodbye":
        close_program()
    user_input = user_input.lower()
    if "hello" in user_input:
        return generate_response("greeting")
    elif "bye" in user_input or "goodbye" in user_input:
        return generate_response("farewell")
    else:
        return generate_response("unknown")

def close_program():
    print("Goodbye! Have a wonderful day!")
    exit()

def generate_response(intent_name):
    responses = {
        "greeting": "Hello! How can I assist you today?",
        "farewell": "Goodbye! Have a wonderful day!",
        # Add more responses as needed
    }
    return responses.get(intent_name, "I'm sorry, I don't understand.")