from unidecode import unidecode

with open('vader_lexicon.txt', 'r') as myfile:
  data = myfile.read()
  text = unidecode(data)
  text_file = open("test.txt", "w")
  text_file.write(text)
  text_file.close()