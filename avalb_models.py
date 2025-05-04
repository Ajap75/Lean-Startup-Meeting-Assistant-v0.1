from openai import OpenAI
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()

client = OpenAI()

# List available models
models = client.models.list()
for m in models.data:
    print(m.id)
