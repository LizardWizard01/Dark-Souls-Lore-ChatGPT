from configparser import ConfigParser

import config
import os
import openai

config = ConfigParser()
config.read('config.cfg')
# openai.api_key_path = 'config.cfg'
API_KEY = config.get('openai', 'api_key')
openai.api_key = API_KEY
print(openai.Model.list())

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a completion
completion = openai.Completion.create(model="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)