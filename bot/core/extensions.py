from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Extension(ABC):
    @abstractmethod
    def process_message(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process message and return updated context"""
        pass

class ExtensionManager:
    def __init__(self):
        self.extensions: List[Extension] = []

    def register(self, extension: Extension):
        self.extensions.append(extension)

    def process_message(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        for extension in self.extensions:
            context = extension.process_message(message, context)
        return context