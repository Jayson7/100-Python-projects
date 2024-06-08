
from googletrans import Translator
text = 'Hallo, mein Name ist Jayson und ich schreibe Apps sowohl in Python als auch in Javascript, was ist mit dir?'

translator = Translator()
# detect the language of the text
detects = translator.detect(text)
print(detects)
translated = translator.translate(text, dest='en')
print(translated.text)