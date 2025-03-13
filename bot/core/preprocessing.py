import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from .extensions import Extension
from typing import Dict, Any

class TextPreprocessor(Extension):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('stopwords', quiet=True)

    def preprocess_text(self, text: str) -> str:
        tokens = nltk.word_tokenize(text.lower())
        cleaned = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token.isalnum() and token not in self.stop_words
        ]
        return ' '.join(cleaned)

    def process_message(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        context['processed_text'] = self.preprocess_text(message)
        return context