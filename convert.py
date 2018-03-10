import os



#not tested : already we have trained data of ocr for all indic language , converter method takes image (with path ) as input
# and runs on 3 different ocrs , because we dont know what language is in image , and produces output file india.txt which contains the translated result may be any language among 3 ( hindi , english , tamil )

def converter(img):
	os.popen('tesseract '+ img +' india -l en')
	os.popen('tesseract '+ img +' india -l tam')
	os.popen('tesseract '+ img +' india -l hin')

