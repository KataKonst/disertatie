import jsonlines
from mongo.imdbService import ImdbService
import glob


imdbService = ImdbService()
i =0

def readFile(file, sentiment, type):
    f = open(file, 'r')
    message = f.read()
    if len(message.split()) < 150:
        imdbService.addWithSentiment({"text": message}, sentiment, type)
    f.close()

path = "/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/tf/"
fileList = glob.glob(path+"train/neg/*.txt")
print(path+"train/neg/*.txt")
for file in fileList:
    i=i+1
    readFile(file,"negative", "train")

print("Review: " + str(i))

fileList = glob.glob(path+"train/pos/*.txt")
for file in fileList:
    i=i+1
    readFile(file, "positive", "train")

print("Review: " + str(i))

fileList = glob.glob(path+"test/neg/*.txt")
for file in fileList:
    i=i+1
    readFile(file, "negative", "test")

print("Review: " + str(i))

fileList = glob.glob(path+"test/pos/*.txt")
for file in fileList:
    i=i+1
    readFile(file, "positive", "test")

imdbService.add()
print("Review: " + str(i))

print("boss")