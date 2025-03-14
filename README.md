# Chatbot

A simple chatbot implemented in Python, enhanced with JavaScript.

## Compatibility

- Python 3.8+
- Node.js 16+
- Windows/Linux/macOS
- Modern browsers (Chrome, Firefox, Edge, Safari)
- SQLite database (included)

## Getting Started

### Prerequisites

- Python 3
- Node.js
- npm

### Installing

1. Clone the repository
   ```sh
   git clone https://github.com/your-username/chatbot.git
   ```
2. Navigate to the project directory
   ```sh
   cd chatbot
   ```
3. Install the Python dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Navigate to the `js` directory and install the Node.js dependencies
   ```sh
   cd js
   npm install
   ```

### Running the Chatbot

1. Start the Python backend:
```sh
python main.py
```

2. In a new terminal, start the Node.js server:
```sh
cd js
npm start
```

3. Access the web interface at:
`http://localhost:3000`

**Example Usage:**
```sh
User: Hello
Bot: Hi there! How can I help you today?
User: What's the weather?
Bot: I can check the weather for any location.
```

### Running Tests

```sh
pytest
```
