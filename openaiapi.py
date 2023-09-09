import os
import openai

openai.api_key = "YOUR_API_KEY"

def chat_completion(task, content):
  completion = openai.ChatCompletion.create(
    max_tokens=len(content)//2,
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a writing assistant who helps with grammar, restructuring sentences, etc."},
      {"role": "user", "content": task + " this sentence - " + content }
    ]
  )
  return completion.choices[0].message

# print(chat_completion("restructure", "I need to see the details now immediately"))
# print(chat_completion("correct the grammar of", "Myself name is Sharang"))