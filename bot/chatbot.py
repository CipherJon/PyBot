import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# Download NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

class Chatbot:
    def __init__(self, intents_file_path='data/intents.json'):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.intents = self.load_intents(intents_file_path)
        self.model = self.train_model()

    def load_intents(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    def preprocess_text(self, text):
        # Tokenize and lemmatize
        tokens = nltk.word_tokenize(text.lower())
        cleaned = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token.isalnum() and token not in self.stop_words
        ]
        return ' '.join(cleaned)

    def train_model(self):
        # Prepare training data
        X = []
        y = []
        for intent in self.intents:
            for pattern in intent['patterns']:
                X.append(self.preprocess_text(pattern))
                y.append(intent['tag'])

        # Create and train pipeline
        model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LinearSVC(dual=False))
        ])
        model.fit(X, y)
        return model

    def get_intent(self, message):
        processed = self.preprocess_text(message)
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