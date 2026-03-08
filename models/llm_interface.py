import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()

# Initialize the client pointing to OpenRouter instead of OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def ask_llm(prompt: str) -> str:
    """Sends the prompt to OpenRouter and returns the AI's response."""
    try:
        response = client.chat.completions.create(
            # Using a highly capable free model on OpenRouter
            model="meta-llama/llama-3.3-70b-instruct:free", 
            messages=[
                {
                    "role": "system", 
                    "content": "You are CodeAOIS, an expert AI developer assistant. Write clean, concise code. If the user asks for code, ONLY output the code without markdown formatting (like ```python) so it can be written directly to a file. If the user is just saying hello or asking a question, reply conversationally."
                },
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error contacting AI Brain: {e}"