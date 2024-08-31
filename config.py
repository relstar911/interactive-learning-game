import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if not self.openai_api_key:
            print("Error: OPENAI_API_KEY not found in environment variables. Please check your .env file.")

    def get(self, key, default=None):
        if key == 'openai_api_key':
            return self.openai_api_key
        # ... Logik für andere Konfigurationsoptionen ...
        return default

config = Config()