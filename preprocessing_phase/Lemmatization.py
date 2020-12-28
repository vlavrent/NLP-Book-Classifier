import spacy
import pandas as pd
from google.colab import drive

drive.mount('drive',force_remount=True)


books = pd.read_csv(r"Processed-Books.csv",encoding="cp1253")
data = books.dropna()

nlp = spacy.load('el')


data['Περιεχόμενα'] = data['Περιεχόμενα'].apply(lambda x: ' '.join([w.lemma_ for w in nlp(x)]))


data.to_csv("Lemma.csv",index=False)
!cp Lemma.csv "drive/My Drive/"