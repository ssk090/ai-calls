import os
from pathlib import Path
from pyexpat.errors import messages
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model="qwen/qwen3.8-27b"

prompt1 = "Hi!"
prompt2 = "What is the capital of India?"
prompt3 = "explain the theory of relativity in 1000 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant."
    }

    user_message = {
        "role": "user",
        "content": prompt
    }
    
    messages = [system_message, user_message]
    response = client.chat.completions.create(model=model,messages=messages, temperature=0.7)
    usage = response.usage
    print(f"Prompt: {prompt} --> Completion tokens: {usage.completion_tokens}, Prompt tokens: {usage.prompt_tokens}, Total tokens: {usage.total_tokens}")

# ## System Prompt
# system_message = {
#     "role": "system",
#     "content": "You are a helpful assistant."
# }

# user_message = {
#     "role": "user",
#     "content": "what is the capital of India ?" ## ask question here   
# }

# messages = [system_message, user_message]

# response = client.chat.completions.create(model=model,messages=messages, temperature=0.7)
# answer = response.choices[0].message.content

# print(answer)
