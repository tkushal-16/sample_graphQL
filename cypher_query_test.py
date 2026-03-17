from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Load the variables from .env into the environment
load_dotenv()

openrouter_base_url = os.getenv("OPENROUTER_URL")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
  base_url=openrouter_base_url,
  api_key=openrouter_api_key,
)

# First API call with reasoning
response = client.chat.completions.create(
  model="openai/gpt-oss-120b:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message
print("Assistant's answer:", response.content)

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="openai/gpt-oss-120b:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

print("Assistant's follow-up answer:", response2.choices[0].message.content)


"""
sample output:
Assistant's answer: The word **“strawberry”** contains **3** occurrences of the letter **r**.
Assistant's follow-up answer: Let's count the letters one by one:

**strawberry** → s t **r** a w b e **r** **r** y  

- The first “r” appears as the 3rd letter.  
- The second “r” appears as the 8th letter.  
- The third “r” appears as the 9th letter.

So there are **3 occurrences of the letter “r”** in “strawberry.”
"""