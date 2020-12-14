import pandas as pd

import spacy
nlp = spacy.load('el_core_news_sm') #pretrained statistical model fro Greek
books = pd.read_csv("../clear_phase/Processed-Books.csv")

books = books.head(10) #so as to compute quickly



def lemmatize(books):


    tokenized_books = books
    periexomena = []

    for desc in tokenized_books['Περιεχόμενα']:
        descInToken = []
        #print(desc)
        token = nlp(desc)

        for w in token:
            #print(w,w.lemma_)
            descInToken.append(w.lemma_) #gia kathe leksi vrisko to lemma tis

        periexomena.append(descInToken)

    #print(periexomena)
    tokenized_books['Περιεχόμενα'] = periexomena # gia kathe perigrafi vazo oles tis lekseis me ta lemmata tous

    return tokenized_books
#tb = tokenize(books)

tb = lemmatize(books)

#print(tb['Περιεχόμενα'])