import os
from openai import OpenAI

OPENAI_API_KEY = "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",

client = OpenAI(
 # This is the default and can be omitted
    api_key=os.environ.get(f"{OPENAI_API_KEY}"),
)

chat_completion = client.chat.completions.create(
 messages=[
 {
 "role": "user",
 "content": "Say this is a test",
 }
 ],
 model="gpt-3.5-turbo",
)