import pandas as pd
import spacy
# nlp = spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")

# 2023-04-07 ebb: Let's pull the data from a trimmed version of your spreadsheet
# (I save this as dsexcel-trimmed.xlsx. We use Pandas as pd for loading an Excel spreadsheet
df = pd.read_excel('dsexcel-trimmed.xlsx', header=None, skiprows=1)
# To make our network TSV we want:
# item name, item type(?), description
# We want to send the blob of text in each description to NLP to see what names are referenced.
# Then output a new TSV as (using column names on left):
# Name  (ItemType)  -- connected by Desc --  NLP entity (Type)
df = df.iloc[:, [1, 4, 7]]  # ebb: Select columns to read, start counting from zero
# print(df)

rows = []
for row in df.iterrows():
    doc = row[1][7]
    # print(doc)
    stringDesc = str(doc)
    tokens = nlp(stringDesc)
    # This should run spaCy nlp over each row, the third (description) column that we imported
    for ent in tokens.ents:
        new_row = [row[1][4], row[1][1], 'connected to', ent.text, ent.label_]
        print(new_row)
        rows.append(new_row)

# ebb: Let's output this as a TSV with network data!
# First we send it to Pandas data frames to make a nice grid structure:
# Create a new DataFrame with the named entities
result = pd.DataFrame(rows, columns=['Name', 'Type', 'Connection', 'Named Entity', 'Entity Type'])

# Output the result as TSV
result.to_csv('darksouls-network.tsv', sep='\t', index=False)


