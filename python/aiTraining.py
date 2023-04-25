from configparser import ConfigParser
# read about input and output formats and import spreadsheet data
import config
import os
import openai
from openai import FineTune
import subprocess
# localTraining = 'fine-tune-testing1.jsonl'


config = ConfigParser()
config.read('config.cfg')
# openai.api_key_path = 'config.cfg'
API_KEY = config.get('openai', 'api_key')
openai.api_key = API_KEY
# print(openai.Model.list())


# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# ebb: I think we were missing a step to retrieve a model.
# print(openai.Model.retrieve("ada:ft-digit-psb-2023-04-21-00-27-58"))

# create a completion
# completion = openai.Completion.create(model="ada:ft-digit-psb-2023-04-21-00-27-58", prompt="You are an assistant that generates new items that could function within the dark souls lore, but is entirely fictional and is not actually in the game")
completion = openai.ChatCompletion.create(
    model="ada:ft-digit-psb-2023-04-21-00-27-58",
    messages=[
        {"role": "system", "content": "Your purpose is to generate new items that could function in the Dark Souls Universe" },
        {"role": "user", "content": "Create a new item"},
    ])


# print the completion


#
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are an assistant that generates new items that could function within the dark souls lore, but is entirely fictional and is not actually in the game"},
#     # {"role": "system", "content":},
#     {"role": "user", "content": "What is your function?"}
#   ])

# openai.File.create(
#   file=open("ds-text.jsonl", "rb"),
#   purpose='fine-tune'
# )
# ebb: old version for preparing the JSONL data from JSON: command = ["openai", "tools", "fine_tunes.prepare_data", "-f", localTraining]
# new version is for handling the training: see if this works.

# ebb: This reproduces CLI functionality in Python
# command = ["openai", "api", "completions.create", "-m", "ada:ft-digit-psb-2023-04-21-00-27-58", "-p", "make a new ring"]

# subprocess.run(command, check=True)


# ebb: The lines above prepare the JSONL file from JSON.

# openai.fine_tunes.create -t "fine-tune.json" -m 'ada'
# openai.FineTune.create(training_file="fine-tune.json")
print(completion.choices[0])
