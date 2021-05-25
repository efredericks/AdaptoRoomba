from sense_hat import SenseHat
import pygame
import random
import os
import pycreate2
import time

# HOLD R + START FOR PAIRING MODE

path = {
  "left": [200, 0, 4],
  "right": [0, 200, 4],
  "forward": [200, 200, 3],
  "reverse": [-200, -200, 3],
  "stop": [0, 0, 1]
}


def moveBot(direction):
  global bot
  bot.drive_direct(path[direction][0], path[direction][1])
  time.sleep(path[direction][2])
  bot.drive_direct(path["stop"][0], path["stop"][1])
  time.sleep(path["stop"][2])

"""
def light(direction, r, c, er, ec):
  if (direction == "right"):
    r += 1
  elif (direction == "left"):
    r -= 1
  elif (direction == "up"):
    c -= 1
  elif (direction == "down"):
    c += 1
  else:
    return r, c

  # clamp
  r = max(0, min(r, 7))
  c = max(0, min(c, 7))
  return r, c
"""
os.environ["SDL_VIDEODRIVER"] = "dummy"

config_mapping = {
  "a": 0,
  "y": 4,
  "x": 3,
  "b": 1,
  "r": 7,
  "l": 6,
  "start": 11,
  "select": 10,
}

pygame.init()
pygame.joystick.init()
bot = pycreate2.Create2(port="/dev/ttyUSB0", baud=115200)

bot.start()
bot.safe()


r = 255
g = 255
b = 255
RED = (r,0,0)
GREEN = (0,g,0)
CLEAR = (0,0,0)

sense = SenseHat()

done = False
clock = pygame.time.Clock()

joystick_count = pygame.joystick.get_count()
print("Joysticks: {0}".format(joystick_count))
assert joystick_count == 1
joystick = pygame.joystick.Joystick(0)
joystick.init()

row = 0
col = 0
"""
exit_row = random.randint(0,7)
exit_col = random.randint(0,7)
while exit_row == row and exit_col == col:
  exit_row = random.randint(0,7)
  exit_col = random.randint(0,7)
"""
update = True

curr_path = [0, 0]
while not done:
  if update:
    sense.clear()
    """
    sense.set_pixel(exit_row, exit_col, (255,0,255))
    sense.set_pixel(row, col, random.randint(0,255), random.randint(0,255),random.randint(0,255))
    update = False

    if ((exit_row == row) and (exit_col == col)):
      sense.show_message("YAY")

      exit_row = random.randint(0,7)
      exit_col = random.randint(0,7)
      while exit_row == row and exit_col == col:
        exit_row = random.randint(0,7)
        exit_col = random.randint(0,7)
      update = True
    """

  #print(curr_path)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
#    elif event.type == pygame.JOYBUTTONDOWN:
#        print("button pressed - {0}".format(event))
    elif event.type == pygame.JOYBUTTONUP:
      if event.button == config_mapping["a"]:
#        curr_path[0] = path["right"][0]
#        curr_path[1] = path["right"][1]
        if (curr_path[0] == 0) and (curr_path[1] == 0):
          curr_path[0] = -path["right"][1]
          curr_path[1] = path["right"][1]
        else:
          if (curr_path[0] > 0): #forward
            curr_path[0] -= 100
          else: # backward
            curr_path[1] -= 100

        #path = moveBot("right")
        #row, col = light("right", row, col, exit_row, exit_col)
        #update = True
      if event.button == config_mapping["y"]:
        if (curr_path[0] == 0) and (curr_path[1] == 0):
          curr_path[0] = path["left"][0]
          curr_path[1] = -path["left"][0]
        else:
          if (curr_path[0] > 0): #forward
            curr_path[1] -= 100
          else: # backward
            curr_path[0] -= 100

        #path = moveBot("left")
        #row, col = light("left", row, col, exit_row, exit_col)
        #update = True
      if event.button == config_mapping["x"]:
        curr_path[0] = path["forward"][0]
        curr_path[1] = path["forward"][1]
        #path = moveBot("forward")
        #row, col = light("up", row, col, exit_row, exit_col)
        #update = True
      if event.button == config_mapping["b"]:
        curr_path[0] = path["reverse"][0]
        curr_path[1] = path["reverse"][1]
        #path = moveBot("reverse")
        #row, col = light("down", row, col, exit_row, exit_col)
        #update = True
      if event.button == config_mapping["start"]:
        bot.drive_stop()
        curr_path[0] = 0
        curr_path[1] = 0
        time.sleep(0.1)
        #row, col = light("clear", row, col, exit_row, exit_col)
        #update = True
      if event.button == config_mapping["select"]:
        bot.drive_stop()
        curr_path[0] = 0
        curr_path[1] = 0
        time.sleep(0.1)
        done = True

    if (curr_path[0] != 0) and (curr_path[1] != 0):
      bot.drive_direct(curr_path[0], curr_path[1])
    else:
      bot.drive_stop()



#    for i in range(joystick.get_numbuttons()):
#      if (joystick.get_button(config_mapping["a"])):
#        row, col = light("right", sense, row, col)
#      if (joystick.get_button(config_mapping["y"])):
#        row, col = light("left", sense, row, col)
#      if (joystick.get_button(config_mapping["x"])):
#        row, col = light("up", sense, row, col)
#      if (joystick.get_button(config_mapping["b"])):
#        row, col = light("down", sense, row, col)



  clock.tick(10)

"""
done = 2000#55
while done > 0:
  sense.clear()

  row = random.randint(0,7)
  col = random.randint(0,7)

  sense.set_pixel(row, col, random.randint(0,255), random.randint(0,255),random.randint(0,255))

  done -= 1
"""
sense.clear()
