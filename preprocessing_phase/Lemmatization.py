import spacy
import pandas as pd
from google.colab import drive

#-------Mounting (connecting to)  drive------
drive.mount('drive',force_remount=True)

#-------Load Data and Remove Null values-------------------
books = pd.read_csv(r"Processed-Books.csv",encoding="cp1253")
data = books.dropna()

#-----------Load el_core_news_sm from spacy----------
nlp = spacy.load('el_core_news_sm')

#------------Lemmatize words----------------------------
data['Περιεχόμενα'] = data['Περιεχόμενα'].apply(lambda x: ' '.join([w.lemma_ for w in nlp(x)]))

#-----------Save Lemmatized dataset to a CSV file on google drive-----------------------
data.to_csv("Lemma.csv",index=False)
!cp Lemma.csv "drive/My Drive/"
