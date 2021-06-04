# https://www.egr.msu.edu/classes/ece480/capstone/spring15/group02/assets/docs/nsappnote.pdf
import struct
import serial

connection = None

VELOCITY_CHANGE = 200
ROTATION_CHANGE = 300

def sendCommandRaw(command):
  global connection

  try:
    if connection is not None:
      connection.write(command)
    else:
      print("Not connected!")
  except serial.serialException:
    print("Lost connection!")
    connection = None

  print(' '.join([str(ord(c)) for c in command]))

def onConnect():
  global connection
  port = "/dev/ttyUSB0"

  try:
    connection = serial.Serial(port, baudrate=115200, timeout=1)
    print("Connected")
  except serial.SerialException:
    print("Failed to connect")

def onQuit():
  return

if __name__ == "__main__":
  onConnect()
