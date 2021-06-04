# https://www.instructables.com/QR-Code-Scanner-Using-OpenCV-in-Python/

# requires libzbar-dev
# opencv-4.2-dev
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
  ret, frame = cap.read()

  for barcode in decode(frame):
    d = barcode.data.decode('utf-8')
    print(barcode.data, d)

