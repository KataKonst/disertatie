import os
from googletrans import Translator
import time
from unidecode import unidecode
import json
import glob
import ntpath

translator = Translator()
fileList = glob.glob("/home/katakonst/Downloads/aclImdb/test/neg/*.txt")
os.makedirs("/home/katakonst/Downloads/ro/test/neg")
for filename in fileList:
    try:
        f = open(filename, 'r')
        message = f.read()
        words=message.split()
        if len(words) < 150:
            time.sleep(1)
            print(filename)
            text = translator.translate(message, dest='ro', src="en")
            txt = text.text
            file = open("/home/katakonst/Downloads/ro/test/neg/"+ntpath.basename(filename), "w")
            file.write(unidecode(txt.lower()))
            file.close()

        f.close()
    except json.decoder.JSONDecodeError:
     print("error")
