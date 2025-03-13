from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from typing import List, Dict, Any

class SVCModel:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LinearSVC(dual=False))
        ])

    def train(self, intents: List[Dict[str, Any]]) -> Pipeline:
        X = []
        y = []
        for intent in intents:
            for pattern in intent['patterns']:
                X.append(pattern)
                y.append(intent['tag'])
        return self.pipeline.fit(X, y)

    def predict(self, text: str) -> str:
        return self.pipeline.predict([text])[0]