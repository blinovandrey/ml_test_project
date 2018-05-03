import pandas as pd
from langdetect import detect

def detect_en_lang(title, description):
    try:
        return detect(title) == 'en' and detect(description) == 'en'
    except:
        return False

    
cavideos = pd.read_csv('dataset/CAvideos.csv')
devideos = pd.read_csv('dataset/DEvideos.csv')
frvideos = pd.read_csv('dataset/FRvideos.csv')
gbvideos = pd.read_csv('dataset/GBvideos.csv')
usvideos = pd.read_csv('dataset/USvideos.csv')
dataset = pd.DataFrame()
dataset = dataset.append(cavideos).append(devideos).append(frvideos).append(gbvideos).append(usvideos)
dataset = dataset[dataset.apply(lambda x: detect_en_lang(str(x['title']), str(x['description'])), axis=1)]
dataset.count()