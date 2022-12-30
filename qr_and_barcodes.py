import numpy as np
from pyzbar.pyzbar import decode
import cv2

img = cv2.imread("myqr.png")

code = decode(img)

print(code)

for barcode in decode(img):
    print(barcode.data) # in bytes
    text = barcode.data.decode('utf-8')
    print(text)
    print(barcode.rect) # the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height.
    
    