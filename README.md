# Simple Chat Bot

This is a simple chat bot written in Python. It uses predefined intents and responses to interact with users.

## File Structure

```
chatbot/
│
├── main.py
├── bot/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── responses.py
│   └── utils.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   └── intents.json
├── logs/
│   └── bot.log
├── tests/
│   ├── __init__.py
│   ├── test_chatbot.py
│   └── test_responses.py
└── requirements.txt
```

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the chat bot:
   ```sh
   python main.py
   ```

5. Run the tests:
   ```sh
   python -m unittest discover tests
   ```

## Usage

Run the chat bot using:
```sh
python main.py
```

Interact with the bot by typing messages. Type `exit`, `quit`, or `bye` to end the conversation.

## Logs

Logs are stored in the `logs/bot.log` file. These logs include user inputs and bot responses.
