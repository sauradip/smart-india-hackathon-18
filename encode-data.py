# Take an image, extract text, and encode it as metadata
import json
import pyexiv2
import cv2
from PIL import Image, ImageFilter
import pytesseract
import argparse
import os

def readtext(file_name):
    index, text = 0, ""
    img = cv2.imread(file_name)
    img_final = cv2.imread(file_name)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation
    image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)
        if w < 30 and h < 30:
            continue
        # cv2.rectangle(img, (x, y), (x + w, y + h), (2, 0, 255), 2)

        cropped = img_final[y :y +  h , x : x + w]
        temp = file_name + '/crop_' + str(index) + '.jpg'
        cv2.imwrite(temp , cropped)
        index = index + 1
        text += pytesseract.image_to_string(Image.open(temp)) # append extracted text to the string

    return text 

def gettext(image):
    # This will call the necessary functions, put original text and translated text into a tuple and return that tuple text
    ext = readtext(image)
    translated = convert(ext)
    text = (ext, translated)
    return text

text = gettext("image")
metadata = pyexiv2.ImageMetadata("image")
metadata.read()
textdata = {
    "Original": text[0],
    "Translated": text[1]
}
metadata['Exif.Photo.UserComment'] = json.dumps(textdata)
metadata.write()
