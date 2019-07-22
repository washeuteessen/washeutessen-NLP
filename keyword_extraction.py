import pymongo
from gensim.summarization import keywords

text = "Hallo, ich heiße Magdalena. Vielleicht sind in diesem Satz gar keine wichtigen Stichwörter enthalten."

print(keywords(text))