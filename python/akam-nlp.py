import spacy
from collections import Counter
import os
# nlp = spacy.cli.download("en_core_web_lg")
# Uncomment this line if you need the language model.
# If you already have it, comment it out.
# Let's try the different spaCy language models for this. We can compare _lg with _md or _sm
nlp = spacy.load("en_core_web_lg")

# workingDir = os.getcwd()
# print("current working directory: " + workingDir)
# # os.listdir lists files and folders inside a path:
# insideDir = os.listdir(workingDir)
# print("inside this directory are the following files AND directories: " + str(insideDir))
#
# CollPath = os.path.join(workingDir, 'dsexcel-text-nlp.txt')
# print(CollPath)

def readTextFiles(filepath):
    readFile = filepath.read()
    # print(readFile)
    stringFile = str(readFile)
    # lengthFile = len(readFile)
    # print(lengthFile)
    tokens = nlp(stringFile)
    # print(tokens)
    listEntities = entitycollector(tokens)
    print(listEntities)
    # cardinal_freq = Counter(listCardinals)
    # topTen = cardinal_freq.most_common(10)
    # print(topTen)



def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        # if entity.label_ == "CARDINAL":
        print(entity.text, entity.label_, spacy.explain(entity.label_))
        entities.append(entity.text)
    return entities


# for file in os.listdir(CollPath):
#     if file.endswith(".txt"):
#         filepath = f"{CollPath}/{file}"
#         print(filepath)
#         readTextFiles(filepath)





# print(listCardinals)
# cardinal_freq = Counter(listCardinals)
# topTen = cardinal_freq.most_common(10)
# print(topTen)

souls = open('dsexcel-text-nlp.txt', 'r', encoding='utf8')
readTextFiles(souls)

# def sentenceLengths(sentences):
#     lengths = []
#     for s in sentences:
#         length = len(s.text)
#         lengths.append(length)
#     return sorted(lengths)


# grimmLengths = sentenceLengths(grimmmSentences)
# # print(grimmLengths)
# maxVal = max(grimmLengths)
# minVal = min(grimmLengths)
# print('The shortest sentence is ' + str(minVal) + ' characters long.')
# print('The longest sentence is ' + str(maxVal) + ' characters long.')

# for sentence in grimmNLP.sents:
# #    print(sentence.text)
#     length = len(sentence.text)
#     if length == minVal:
#         print("The shortest sentence is: " + sentence.text)
#     if len(sentence.text) == maxVal:
#         print('The longest sentence is: ' + sentence.text + ' :' + str(maxVal) + 'characters')

lines = [print(entity.text, entity.label_, spacy.explain(entity.label_))]
with open('itemsOutput.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')