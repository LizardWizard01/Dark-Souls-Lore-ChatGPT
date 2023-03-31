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
    # return listEntities
    # print(len(listEntities))
    # # cardinal_freq = Counter(listCardinals)
    # # topTen = cardinal_freq.most_common(10)
    # # print(topTen)
    # file = open('itemsOutput.txt', 'w')
    # for entity in listEntities:
    #     print(entity)
    #     file.write(entity)
    #     file.write(entity.label_)
    #     file.write('\n')
    # file.close()
    with open('itemsOutput.txt', 'w') as f:
        entities = []
        for entity in tokens.ents:
            # OLD VERSION print(entity.text, entity.label_, spacy.explain(entity.label_))
# NEW VERSION: MAKE IT A LIST:
            entityInfo = [entity.text, entity.label_, spacy.explain(entity.label_)]
            stringify = str(entityInfo)
            print(stringify)
            f.write(stringify)
            f.write('\n')
# TSA: This works much better, I can now get output for each item now that it is a list.

def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        # if entity.label_ == "CARDINAL":
        print(entity.text, entity.label_, spacy.explain(entity.label_))
        # Attribute error 'dict' object has no attribute 'append'

        entities.append(entity.text)
    return entities
    print(entities)

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




