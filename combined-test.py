# https://www.instructables.com/QR-Code-Scanner-Using-OpenCV-in-Python/
# https://atsushisakai.github.io/PyRoombaAdapter/

# requires libzbar-dev
# opencv-4.2-dev
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
from pyroombaadapter import PyRoombaAdapter
from time import sleep

# Roomba
PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)


# Video
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
  ret, frame = cap.read()

  for barcode in decode(frame):
    data = barcode.data.decode('utf-8')
    data = data.lower()

    adapter.change_mode_to_full()

    if data == "hazard":
      print("Hazard spotted, adapting")
      adapter.send_song_cmd(0, 9,
              [69, 69, 69, 65, 72, 69, 65, 72, 69],
              [40, 40, 40, 30, 10, 40, 30, 10, 80])
      adapter.send_play_cmd(0)
      sleep(10.0)
      break

    elif data == "start":
      print("Driving for 2s")
      adapter.change_mode_to_full()
      adapter.move(0.1, 0.0)
      #adapter.send_drive_direct(100, 100)
      sleep(2.0)
      break

    elif data == "stop":
      print("Stopping")
      #adapter.move(0.0, 0.0)
      adapter.change_mode_to_safe()
      adapter.send_drive_direct(0, 0)
      sleep(1.0)
      break

    else:
      print("Not implemented - [{0}]".format(data))
      break

    #elif data == "stop":
    #  adapter.
    #print(barcode.data, d)

