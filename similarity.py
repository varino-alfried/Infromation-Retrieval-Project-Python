import numpy as np
import pandas as pd


def tokenize(query):
    stopword = ['the', 'a', 'an', 'in','of','that','then','is','are','was','were','out','to',',','.','as','and']
    tokens = query.split()
    tokens_without_stop_word = [word.lower() for word in tokens if not word in stopword]
    return  tokens_without_stop_word
def cosine_similarity(x, y):
    x_sqrt = np.sqrt(np.dot(x, x))
    y_sqrt = np.sqrt(np.dot(y, y))
    if y_sqrt != 0:
        return (np.dot(x,y.T) / (x_sqrt * y_sqrt))
    elif y_sqrt == 0:
        return 0
doc2vocab  = dict()
vocab2doc  = dict()
for i in range(1, 11):
    doc2vocab[i] = dict()

    with open('%d.txt' % i, 'r', encoding="utf-8") as doc:
        read_string = doc.read()
        read_string = read_string.lower()
        tokens = tokenize(read_string)

        for words in tokens:
            # make document and vocab pair dictionary
            if words in doc2vocab[i]:
                doc2vocab[i][words] += 1

            else:
                doc2vocab[i][words] = 1

            # make inverted index, {word : [doc1, doc3, ... ]}
            text_str = 'doc'+str(i)
            if words in vocab2doc:
                if text_str not in vocab2doc[words]:
                    vocab2doc[words].append(text_str)

            else:
                vocab2doc[words] = list()
                vocab2doc[words].append(text_str)

term_pd = pd.DataFrame.from_dict(doc2vocab, orient='index')
term_pd = term_pd.fillna(0)

def doc_tf_idf(dataframe,query):

    _, width = dataframe.shape
    final = list()

    new_tf = dataframe
    doc_term_value = dataframe[dataframe > 0].count().values
    doc_frequency = np.log(60 / (doc_term_value ))

    for i in range(len(dataframe)):
        results = np.zeros(width)
        one_row = dataframe.iloc[i]
        row_value = one_row.values
        row_index = one_row.index

        for j,term in enumerate(row_index):
            if row_value[j] > 0:
                term_frequency = 1+np.log(row_value[j])
                new_tf.iloc[i,j] = term_frequency * doc_frequency[j]

            elif row_value[j] == 0:
                term_frequency = 0
                new_tf.iloc[i,j] = 0

            if term in query:
                new_column = dataframe[[term]]
                new_col_value = new_column[new_column > 0].count().values
                results[j] = term_frequency * (np.log(60 / (new_col_value[0] + 1)))

        final.append((i, cosine_similarity(new_tf.iloc[i].values, results)))



    return new_tf, final
inquery = input("Please enter a query: ")
query = tokenize(inquery)
term_doc_matrix, query_tf_idf = doc_tf_idf(term_pd, query)
score = sorted(query_tf_idf, key = lambda x : x[1], reverse=True)
for ind_file,similarity in score:
    print("File {} query similarty is {}".format(ind_file+1,similarity))