import os
from pathlib import Path
from pyexpat.errors import messages
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model="qwen/qwen3.8-27b"

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

system_message = {
    "role":"system",
    "content": system_prompt
}

text = "Hello, I am having trouble logging into my account. My name is John Doe and my email is john.doe@example.com"

user_message = {
    "role":"user",
    "content": text
}

messages = [system_message, user_message]

response = client.chat.completions.create(model=model, messages=messages, temperature=0.7, response_format=response_format)

answer = response.choices[0].message.content
print(answer)