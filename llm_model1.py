"""
This example demonstrates how to use the reasoning feature in a multi-turn conversation with the OpenAI API.
The LLM name is OpenAI: gpt-oss-20b (free)
Link of OpenRouter: https://openrouter.ai"""


import os
from dotenv import load_dotenv
from openai import OpenAI

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
  model="openai/gpt-oss-20b:free",
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
print("Assistant's response:", response.content)
print("--------------------------------------------------------------")

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
  model="openai/gpt-oss-20b:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)
print("Assistant's response to follow-up:", response2.choices[0].message.content)

"""
This is the sample response of the first API call with reasoning enabled:
Assistant's response: There are **3** r's in the word “strawberry.”
--------------------------------------------------------------
Assistant's response to follow-up: Yes—there are **three** “r” letters in “strawberry.”
If you write it out:

```
s t r a w b e r r y
```

You can see the “r” at positions 3, 8, and 9. So the total count is 3.
"""