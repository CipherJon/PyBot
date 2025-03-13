from bot.core.extensions import Extension, ExtensionManager
from bot.core.preprocessing import TextPreprocessor
from bot.core.models.svc_model import SVCModel
from typing import List, Dict, Any
import json
import random
import nltk

# Download NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

class ResponseHandler(Extension):
    def __init__(self, intents: List[Dict[str, Any]]):
        self.intents = intents

    def process_message(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            processed_text = context.get('processed_text', '')
            intent_tag = context.get('predicted_intent', '')
            
            for intent in self.intents:
                if intent['tag'] == intent_tag:
                    context['response'] = random.choice(intent['responses'])
                    return context
            context['response'] = "I'm sorry, I don't understand."
            return context
        except Exception as e:
            context['response'] = f"Error processing request: {str(e)}"
            return context

class Chatbot:
    def __init__(self, extensions: List[Extension] = None):
        self.extension_manager = ExtensionManager()
        self.preprocessor = TextPreprocessor()
        self.extension_manager.register(self.preprocessor)

        self.intents = self.load_intents('data/intents.json')
        self.model = SVCModel().train(self.intents)
        self.response_handler = ResponseHandler(self.intents)
        self.extension_manager.register(self.response_handler)

        if extensions:
            for extension in extensions:
                self.extension_manager.register(extension)

    def load_intents(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, 'r') as f:
            return json.load(f)

    def get_response(self, message: str) -> str:
        context = {'original_message': message}
        context = self.extension_manager.process_message(message, context)
        return context.get('response', '')

    def train_model(self):
        # Prepare training data
        X = []
        y = []
        for intent in self.intents:
            for pattern in intent['patterns']:
                X.append(self.preprocessor.preprocess_text(pattern))
                y.append(intent['tag'])

        # Create and train pipeline
        model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LinearSVC(dual=False))
        ])
        model.fit(X, y)
        return model

    def get_intent(self, message):
        processed = self.preprocessor.preprocess_text(message)
        return self.model.predict([processed])[0]

    def get_response(self, message):
        try:
            intent_tag = self.get_intent(message)
            for intent in self.intents:
                if intent['tag'] == intent_tag:
                    return random.choice(intent['responses'])
            return "I'm sorry, I don't understand."
        except Exception as e:
            return f"Error processing request: {str(e)}"