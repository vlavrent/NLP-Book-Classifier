import re
import pandas as pd

books = pd.read_csv(r"Books.csv",encoding="cp1253")


#--------Remove Unwanted Columns--------------------
books = books.drop(columns=['Unnamed: 0'])
books = books.drop(index=books[books['Περιεχόμενα'] == '#NAME?'].index)

#---------Remove Null values-------------------------
books = books.dropna()


#----------Remove Punctuation-English words-Numbers----------------
books['Περιεχόμενα'] = books['Περιεχόμενα'].str.replace('\d+([.]\d+)?', '')#Removes floats and Integers
books['Περιεχόμενα'] = books['Περιεχόμενα'].str.findall('\w{4,}').str.join(' ')
books['Περιεχόμενα'] = books['Περιεχόμενα'].str.replace('\w[A-Za-z]+', '')

#-------------------Lowercasing--------------------------------------
books["Περιεχόμενα"] = books["Περιεχόμενα"].apply(lambda x: ' '.join([item.lower() for item in x.split()]))


books.to_csv("Processed-Books.csv",index=False)
