from PIL import Image
#import goslate
from langdetect import detect
from googletrans import Translator

#gs = goslate.Goslate()

# -*- coding: utf-8 -*-
#print(detect("इस वॉशिंग मशीन में कुछ खराबी है।"))
#detect("Ein, zwei, drei, vier")

# india.txt contains the output coming from customised ocr , languages contained in india.txt may vary from english , hindi , tamil , urdu , bengali
separators = [u"।", u",", u"."]
text = open("india.txt").read()

#This converts the encoded text to an internal unicode object, where
# all characters are properly recognized as an entity
text = text.decode("utf-8")

#this breaks the text on the white spaces, yielding a list of words
words = text.split()

counter = 1

output = ""
for word in words:
    #if the last char is a separator, and is joined to the word:
    if word[-1] in separators and len(word) > 1:
        #word up to the second to last char:
        output += word[:-1] +" "
        counter += 1
        #last char
        output += word[-1] +" "
    else:
        output += word +" "
    counter += 1

#detect(output) will return the standard language code of the text in india.txt , if language in india.txt is bengali then it will return 'ben' 
#for hindi it will return 'hin' etc  

print("Input from OCR")
print (output)
print ("language is in "+detect(output))


# translate english>english(not needed) hindi>english urdu>english bengali>english , so destination lang=english


translator = Translator()
translated=translator.translate(output, dest='en')
print("Translation of Input")
print(translated.text)
#translator('ur', 'en', output)
#print(gs.translate(output, 'hi'))
