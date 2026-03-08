import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def ask_llm(prompt: str) -> str:
    """Sends the prompt to OpenRouter and returns the AI's response."""
    try:
        response = client.chat.completions.create(
            # Switched to Qwen 2.5 Coder Free - much more stable for coding tasks
            model="openrouter/free",
            messages=[
                {
                    "role": "system", 
                    "content": "You are CodeAOIS, an expert AI developer assistant. If the user asks for code, ONLY output the raw code without markdown formatting (like ```python) so it can be safely written to a file. If the user is just saying hello or asking a general question, reply conversationally like a human."
                },
                {"role": "user", "content": prompt}
            ],
        )
        # Strip out any lingering markdown blocks the AI might stubbornly add
        content = response.choices[0].message.content
        if content.startswith("```python"):
            content = content.replace("```python\n", "").replace("```", "")
        return content.strip()
    except Exception as e:
        return f"Error contacting AI Brain: {e}"