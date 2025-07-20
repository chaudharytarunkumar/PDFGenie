import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize the following text."},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
