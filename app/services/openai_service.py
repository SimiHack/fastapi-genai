from openai import OpenAI
from app.config import OPENAI_API_KEY

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

async def generate_ai_response(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content