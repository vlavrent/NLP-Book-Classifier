import pandas as pd
import re


def characterToBegin(text):
    if(len(text)>0):
        c = text[0]
        chars = ['>',"<",'[',']','.',',',';','(',')',' ']

        for char in chars:
            if (c == char):
                return True
        return False
def replaces(input):

    #1st phase : remove content in parentheses
    text = input

    text = text.replace("α)","")
    text = text.replace("β)","")
    text = text.replace("γ)","")
    regex = "\((.*?)\)"
    text = re.sub(regex, "", text)

    regex = "\[(.*?)\]"
    text = re.sub(regex, "", text)

    regex = "\[(.*?)\)"
    text = re.sub(regex, "", text)

    regex = "\((.*?)\]"
    text = re.sub(regex, "", text)

    text = text.replace("[...]",'')
    text = text.replace("[. . .]", '')
    text = text.replace("(...)", '')
    text = text.replace("(. . .)", '')

    while (characterToBegin(text) == True):
        text = text[1:]
    return text

def saveToCsv(dataframe,filename):
    dict = {"filosofia":"philosophy","history":"history","logotexnia2":"literature","school":"school","kids":"kids","comic":"comics","education":"education","enasxoliseis":"language","filologia":"philology","geography":"geography","koinoniologia":"sociology","political-economical":"political_economy","psixologia":"psychology","science":"science","texniklp":"art_theater_cinema"}


    luben_name = filename.replace("datasets/books-","").replace(".csv","")

    filename = filename.replace("datasets/","output/").replace(luben_name, str(dict[luben_name]))
    print(filename)
    dataframe.to_csv(path_or_buf=filename,sep=";",index=False)



datasets = ["filosofia","history","logotexnia2","school","kids","comic","education","enasxoliseis","filologia","geography","koinoniologia","political-economical","psixologia","science","texniklp"]
#datasets = ["texniklp"]
def isInEnglishOrBlack(text):
    if(len(text)==0):
        return True
    threshold = 0.5
    textInEnglish = re.findall("[a-z]|[A-Z]",text)
    if(len(textInEnglish)/len(text) > threshold):
        #print(text)
        #print("-----------------")

        return True
    else:
        return False

def isCD(category,text):
    t = type("string")
    if(type(text)== t):
        if (category == "texniklp" and ("CD" in text)):
            return True
        else:
            return False
    else:
        return True

for category in datasets:
    filename = "datasets/books-"+str(category)+".csv"

    data = pd.read_csv(filename,delimiter=";",engine="python", header=None)
    data = data.drop_duplicates()
    indicesToDrop = []
    #print(data)

    count = 0
    for index,row in data.iterrows():
        count += 1
        # print(row[0])
        # print()
        # print(row[1])
        # print(row[p])
        # print(row[2])
        #print(index)
        # print(row[1])
        # print()
        row[1] = replaces(row[1])
        if(isInEnglishOrBlack(row[1]) or isCD(category,row[0])):
            indicesToDrop.append(index)
        #print(row[1])
        # if(count>10):
        #     break
    data = data.drop(indicesToDrop)

    print(data.shape)
    saveToCsv(data,filename)