import os
import openai
from dotenv import load_dotenv
from persona import persona
from elevenlabs import voices,set_api_key,Voice,VoiceSettings,generate,save,VoiceDesign,Gender,Age,Accent



load_dotenv()
os.environ['PATH'] += os.pathsep + "C:/ffmpeg/bin"
set_api_key(os.getenv("ELEVENLABS_API_KEY"))
voice = voices()
print(voice[-1])
openai.api_key = os.getenv("OPENAI_API_KEY")
messages= [{
          "role": "system",
          "content": f"{persona}"
        },]
def generate_audio(response):
    design = VoiceDesign(
    name='Lexa',
    text=response,
    voice_description="A voice resonating from the depths, textured with a rough, gravelly quality, and charged with an intense determination that effortlessly conveys the intricate tapestry of emotions , he talks slowly.",
    gender=Gender.male,
    age=Age.middle_aged,
    accent=Accent.american,
    accent_strength=1.4,
    )
    audio = design.generate()
    
    # audio = generate(
    # text=response,
    # voice=Voice(
    #     voice_id='MYwiFnEo7h6BOxShlxng',
    #     settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    # )
    # )
    save(audio,filename="audio.wav")

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
      generate_audio(response)
      messages.append(ai_content)
      
      reply = ""
      
     
      
if __name__ == "__main__":
   main()