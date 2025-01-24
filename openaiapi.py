import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_completion(task, content):
  completion = openai.ChatCompletion.create(
    temperature=0.2,
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": task + "-" + '"' + content + '"'}
    ]
  )
  return completion.choices[0].message.content