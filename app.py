import os
import openai
from dotenv import load_dotenv
from persona import persona

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
messages= [{
          "role": "system",
          "content": f"{persona}"
        },]
def main():
  def get_response(prompt):
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
      
      response = response.choices[0].message.content
      return response
  
  reply = ""
  while(reply == ""):
      prompt = input("(Type /quit to quit) \n Enter: ")
      reply = prompt
      if prompt =="/quit":
         break
      user_content = {"role": "user","content":prompt}
      messages.append(user_content)
      response = get_response(prompt)
      
      ai_content = {"role": "assistant", "content": response}
      print(response)
      
      messages.append(ai_content)
      
      reply = ""
      
     
      
if __name__ == "__main__":
   main()