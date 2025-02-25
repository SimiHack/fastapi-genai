from openai import OpenAI
from app.config import OPENAI_API_KEY

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

async def generate_ai_response(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    content = response.choices[0].message.content
    if "code" in prompt.lower():
        return f"<pre><code>{content}</code></pre>"
    elif "poem" in prompt.lower():
        return f"<pre>{content}</pre>"
    elif "list" in prompt.lower():
        return f"<ul>{''.join(f'<li>{item}</li>' for item in content.splitlines())}</ul>"
    elif "quote" in prompt.lower():
        return f"<blockquote>{content}</blockquote>"
    elif "table" in prompt.lower():
        rows = content.splitlines()
        table = "<table>" + "".join(f"<tr><td>{'</td><td>'.join(row.split())}</td></tr>" for row in rows) + "</table>"
        return table
    else:
        return content