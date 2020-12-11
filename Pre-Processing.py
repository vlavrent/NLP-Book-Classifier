import pandas as pd
import numpy as np
import nltk


stop = ["τα","η","ο","το","του","την","τους","της","την","αυτο","αυτό","αυτός","αυτος","αυτή",
        "αυτη","αυτά","αυτα","και","ποιος","ποια","ποιος","τη","που","πιο","τις","απο",
        "από","στο","ή","πού","πιό","ποιό","ποιά","ποιός","οι","στα","μας","δεν","πως","πώς",
       "στη","στην","στο","να","ένας","μία","ένα","ενας","μια","ενα","τον","ενός","όσο","για",
       "αλλά","ότι","ό,τι","οτι","άλλον","σαν","απ","πολύ","πολλή","με","έναν","εναν"]

books = pd.read_csv(r"Books.csv",encoding="cp1253")

#--------Remove Unwanted Columns--------------------
books = books.drop(columns=['Unnamed: 0'])
books = books.drop(index=books[books['Περιεχόμενα'] == '#NAME?'].index)

#---------Remove Null values-------------------------
books = books.dropna()

Imbalance = books["Κατηγορία"].value_counts()
Imbalance.plot(kind='bar')

#---------------Remove Punctuation--------------------------------
books["Περιεχόμενα"] = books["Περιεχόμενα"].str.replace('\'''+', '').str.replace('\:+', '').str.replace('\d+', '').str.replace('\?+', '').str.replace('\"+', '').str.replace('\.+', '').str.replace('\,+', '').str.replace('\(+', '').str.replace('\)+', '').str.replace('\«+', '').str.replace('\»+', '').str.replace('\!+', '').str.replace('\-+', '').str.replace('\++', '').str.replace('\#+', '').str.replace('\΄΄;+', '').str.replace('\@+', '')

#-----------------Lowercasing------------------------------------
books["Περιεχόμενα"] = books["Περιεχόμενα"].apply(lambda x: ' '.join([item.lower() for item in x.split()]))


#-----------------Remove Stopwords-------------------------------
books["Περιεχόμενα"] = books["Περιεχόμενα"].apply(lambda x: ' '.join([item for item in x.split() if item not in stop]))


#------------------Remove English Words-------------------------
words = set(nltk.corpus.words.words())
books["Περιεχόμενα"] = books["Περιεχόμενα"].apply(lambda x: ' '.join([item for item in x.split() if item not in words]))

#books.to_csv("Processed-Books.csv",index=False)










