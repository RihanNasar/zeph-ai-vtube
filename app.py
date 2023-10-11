import os
import openai
from dotenv import load_dotenv
from persona import persona
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "what do you think about griffith"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": f"{persona}"
    },
    {
        "role":"assistant",
        "content": f"{prompt}"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0])