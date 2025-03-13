import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = "SimpleBot"
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///users.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False