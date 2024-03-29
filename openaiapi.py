from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_completion(task, content):
  completion = openai.ChatCompletion.create(
    temperature=0.2,
    model="gpt-3.5-turbo",
    messages=[
      # {"role": "system", "content": "Chat is an assistant that helps the user with correcting grammatical mistakes in their text, or restructure sentences to make the meaning of the texts more clear or concise."},
      {"role": "user", "content": task + "-" + '"' + content + '"'}
    ]
  )
  return completion.choices[0].message.content

