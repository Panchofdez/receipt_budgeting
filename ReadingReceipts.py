import cv2
import pytesseract
import itertools

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

img = cv2.imread('Scanned_receit.jpeg')
text = pytesseract.image_to_string(img)

#cleaning up extracted information
splitted_text =text.split()
sorted_list = []

for item in splitted_text:
    if item.find('.')!=-1 and item.find('/')==-1 or item.isupper():
        sorted_list.append(item)

print(sorted_list)
