from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
from threading import Thread, Event

## Thread class to handle robot asynchronously
thread = Thread()
thread_stop_event = Event()

### Things we care about:
# Sensor state
# Wheel velocities
# Song active?

def randomNumberGenerator():
  print("Randomizing")
  while not thread_stop_event.isSet():
    n = round(random.random()*10, 3)
    print("Number: {0}".format(n))
    socketio.emit('newnumber', {'number': n})#, namespace="/test")
    socketio.sleep(5)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hunter12345'
socketio = SocketIO(app)

@socketio.on('connect')#, namespace="/test")
def connect():
  global thread
  emit('after connect', {'data':'user connected'})

  if not thread.isAlive():
    print("Starting new thread")
    thread = socketio.start_background_task(randomNumberGenerator)

@app.route("/")
def index():
  return render_template("index.html", data=random.random())

if __name__ == "__main__":
  socketio.run(app)

