import pandas as pd
from tabulate import tabulate
from nltk.corpus import stopwords

def tokenization(query):
    stopWords = stopwords.words('english')
    tokens = query.split()
    tokensWithoutSW = [word.lower() for word in tokens if not word in stopWords]
    return  tokensWithoutSW

def positionalIndex (tokens):
    positionalindex = dict()
    for pos, term in enumerate(tokens):
        if term in positionalindex:
            positionalindex[term].append(pos + 1)
        else:
            positionalindex[term] = []
            positionalindex[term].append(pos + 1)
    return positionalindex

positions = dict()

inquery = input("Please enter your query: ")
query = tokenization(inquery)

for i in range(1, 11):
    with open('%d.txt' % i, 'r', encoding="utf-8") as doc:
        read_string = doc.read()
        tokens = tokenization(read_string)
        positionalindex = positionalIndex(tokens)
        print(tokens)

        for word in query:
            for pos, term in enumerate(positionalindex):
                if term == word:
                    count = len(positionalindex[word])
                    if word in positions:
                        positions[word][0] = positions[word][0] + count
                        positions[word].append([count,"Doc" + str(i), positionalindex[word]])
                    else:
                        positions[word] = []
                        positions[word].append(count)
                        positions[word].append([count,"Doc" + str(i), positionalindex[word]])

df = pd.DataFrame([positions])
print(tabulate(df, showindex=False, headers=df.columns, tablefmt = 'psql'))
