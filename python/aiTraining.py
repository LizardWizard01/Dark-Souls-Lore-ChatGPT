from configparser import ConfigParser

import config
import os
import openai

config = ConfigParser()
config.read('config.cfg')
openai.api_key_path = 'config.cfg'
API_KEY = config.get('openai', 'api_key')
#Authorization: "Tyler Akam" API_KEY
openai.api_key = API_KEY
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)