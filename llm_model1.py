"""
This example demonstrates how to use the reasoning feature in a multi-turn conversation with the OpenAI API.
The LLM name is OpenAI: gpt-oss-20b (free)
Link of OpenRouter: https://openrouter.ai/api/v1"""


from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
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