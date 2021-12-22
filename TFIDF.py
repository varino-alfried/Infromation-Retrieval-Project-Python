import pandas as pd
import math
from tabulate import tabulate


with open("1.txt", "r") as m, open("2.txt", "r") as h, open("3.txt", "r") as a, open("4.txt", "r") as v, open("5.txt", "r") as q,open("6.txt", "r") as y, open("7.txt", "r") as L, open("8.txt", "r") as I, open("9.txt", "r") as O, open("10.txt", "r") as P:
    documentA = m.read()
    documentB = h.read()
    documentC = a.read()
    documentD = v.read()
    documentE = q.read()
    documentF = y.read()
    documentG = L.read()
    documentH = I.read()
    documentI = O.read()
    documentJ = P.read()

stopWords = stopWords = ['the', 'a', 'an', 'in', 'of', 'that', 'then', 'is', 'are', 'was', 'were', 'out', ',',
                         '.', 'as','']
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
bagOfWordsC = documentC.split(' ')
bagOfWordsD = documentD.split(' ')
bagOfWordsE = documentE.split(' ')
bagOfWordsF = documentF.split(' ')
bagOfWordsG = documentG.split(' ')
bagOfWordsH = documentH.split(' ')
bagOfWordsI = documentI.split(' ')
bagOfWordsJ = documentJ.split(' ')

bagOfWordsAWithoutSW = [word.lower() for word in bagOfWordsA if not word in stopWords]
bagOfWordsBWithoutSW = [word.lower() for word in bagOfWordsB if not word in stopWords]
bagOfWordsCWithoutSW = [word.lower() for word in bagOfWordsC if not word in stopWords]
bagOfWordsDWithoutSW = [word.lower() for word in bagOfWordsD if not word in stopWords]
bagOfWordsEWithoutSW = [word.lower() for word in bagOfWordsE if not word in stopWords]
bagOfWordsFWithoutSW = [word.lower() for word in bagOfWordsF if not word in stopWords]
bagOfWordsGWithoutSW = [word.lower() for word in bagOfWordsG if not word in stopWords]
bagOfWordsHWithoutSW = [word.lower() for word in bagOfWordsH if not word in stopWords]
bagOfWordsIWithoutSW = [word.lower() for word in bagOfWordsI if not word in stopWords]
bagOfWordsJWithoutSW = [word.lower() for word in bagOfWordsJ if not word in stopWords]

uniqueWords = set(bagOfWordsAWithoutSW).union(set(bagOfWordsBWithoutSW)).union(set(bagOfWordsCWithoutSW)).union(
    set(bagOfWordsDWithoutSW)).union(set(bagOfWordsEWithoutSW)).union(set(bagOfWordsFWithoutSW)).union(set(bagOfWordsGWithoutSW)).union(
    set(bagOfWordsHWithoutSW)).union(set(bagOfWordsIWithoutSW)).union(set(bagOfWordsJWithoutSW))

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsAWithoutSW:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsBWithoutSW:
    numOfWordsB[word] += 1
numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsCWithoutSW:
    numOfWordsC[word] += 1
numOfWordsD = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsDWithoutSW:
    numOfWordsD[word] += 1
numOfWordsE = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsEWithoutSW:
    numOfWordsE[word] += 1
numOfWordsF = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsFWithoutSW:
    numOfWordsF[word] += 1
numOfWordsG = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsGWithoutSW:
    numOfWordsG[word] += 1
numOfWordsH = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsHWithoutSW:
    numOfWordsH[word] += 1
numOfWordsI = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsIWithoutSW:
    numOfWordsI[word] += 1
numOfWordsJ = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsJWithoutSW:
    numOfWordsJ[word] += 1



def computeTF(wordDict, bagOfWords):
    tfDict = dict()
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = round(math.log10(1 + (count / float(bagOfWordsCount))), 2)
    return tfDict

print('\n')
print('Term Frequancy for 10 documents: ')

df = pd.DataFrame([numOfWordsA, numOfWordsB, numOfWordsC, numOfWordsD, numOfWordsE,numOfWordsF,numOfWordsG,numOfWordsH,numOfWordsI,numOfWordsJ])
df.index += 1
print(df.T)

def computeIDF(documents):
    import math
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
    return idfDict


idfs = computeIDF([numOfWordsA, numOfWordsB, numOfWordsC, numOfWordsD, numOfWordsE,numOfWordsF,numOfWordsG,numOfWordsH,numOfWordsI,numOfWordsJ])
idfs_items = idfs.items()
print('\n')
print('Inverted Document Frequancy : ')
df = pd.DataFrame([idfs])
print(tabulate(df, showindex=False, headers=df.columns, tablefmt = 'psql'))


print('\n')
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = dict()
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


tfidfA = computeTFIDF(numOfWordsA, idfs)
tfidfB = computeTFIDF(numOfWordsB, idfs)
tfidfC = computeTFIDF(numOfWordsC, idfs)
tfidfD = computeTFIDF(numOfWordsD, idfs)
tfidfE = computeTFIDF(numOfWordsE, idfs)
tfidfF = computeTFIDF(numOfWordsF, idfs)
tfidfF = computeTFIDF(numOfWordsF, idfs)
tfidfG = computeTFIDF(numOfWordsG, idfs)
tfidfH = computeTFIDF(numOfWordsH, idfs)
tfidfI = computeTFIDF(numOfWordsI, idfs)
tfidfJ = computeTFIDF(numOfWordsJ, idfs)

df = pd.DataFrame([tfidfA, tfidfB, tfidfC, tfidfD, tfidfE,tfidfF,tfidfG,tfidfH,tfidfI,tfidfJ])

print('\n')
print('TFIDF for 10 documents: ')
pd.set_option('max_column',None)
df.index += 1
print(df.T)
