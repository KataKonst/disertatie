import os
from googletrans import Translator
import time
from unidecode import unidecode
import  json


translator = Translator()

for filename in os.listdir('/home/katakonst/Downloads/aclImdb/train/neg'):
    try:
        txt=""
        time.sleep(1)
        with open(os.path.join('/home/katakonst/Downloads/aclImdb/train/neg', filename)) as f:
            content = f.read()
            text=translator.translate(content, dest='ro', src="en")
            txt=text.text;
        with open(os.path.join('/home/katakonst/Downloads/aclImdb/train/neg', filename), "w") as f:
            f.write(unidecode(txt.lower()))
            print(unidecode(txt.lower()))
    except json.decoder.JSONDecodeError:
        print("Asd")
