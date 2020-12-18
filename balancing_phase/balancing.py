#from preprocessing_phase import preprocess
import heapq
import nltk
nltk.download('stopwords')
import random

from textblob import TextBlob
from textblob.translate import NotTranslated
#Data Augmentation Technique

stop_words = nltk.corpus.stopwords.words('greek')
with open('stopwords.txt') as f:
    stop_words = f.read().splitlines()


lexicon = ["άντρας","γυναίκα","παιδί"]
emb = {'άντρας': [0.5 , 0.3, 0.2], 'γυναίκα': [0.3 , 0.5 , 0.2], 'παιδί': [0.1 , 0.3 , 0.6]}

text = ['αλλά','άντρας']

def replaceBySynonym(text):
    newText = []
    for word in text:
        if(word in stop_words):
            newText.append(word)
        else:
            synonym_index = [emb[word].index(x) for x in sorted(emb[word], reverse=True)[:2]][1]
            synonym = lexicon[synonym_index]
            newText.append(synonym)

    return newText



def replaceByShuffling(text):
    newText = text.copy()
    random.shuffle(newText)
    return newText

def replaceByTranslation(text):
    newText = []
    sr = random.SystemRandom()
    for word in text:
        wordBlob = TextBlob(word)
        try:
            wordBlob = wordBlob.translate(to="en")  ## Converting to random langauge for meaningful variation
            wordBlob = wordBlob.translate(to="el")
        except NotTranslated:
            pass

        newText.append(str(wordBlob).lower())

    return newText

print(text)
print("converts to: ")
print(replaceBySynonym(text))
print(replaceByShuffling(text))
print(replaceByTranslation(text))