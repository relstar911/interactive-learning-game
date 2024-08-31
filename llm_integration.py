from openai import OpenAI
from config import config

api_key = config.get('openai_api_key')
if not api_key:
    print("Error: OpenAI API key is not set. Please check your .env file and ensure it contains OPENAI_API_KEY=your_api_key_here")
    client = None
else:
    client = OpenAI(api_key=api_key)

def generate_response(prompt):
    if not client:
        return "OpenAI API key is not set. Unable to generate response."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher Assistent in einem Lernspiel."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in generating response: {str(e)}")
        return "Entschuldigung, ich konnte keine Antwort generieren."