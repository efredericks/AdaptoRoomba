import rospy
from std_msgs.msg import Float32, Int16
from create_msgs.msg import ChargingState
import threading

# Simple averaging of list data
def average(data):
  return sum(data)/len(data)
      

class BatteryMonitor():
  def __init__(self, duration):
    self.duration = duration

    ## TODO: do we use the timer as the fusion method?

    # TODO: remove count (just use data.length)
    self.topics = { # topic: {type, callback}
      'battery/capacity':
        {'type'    : Float32, 
         'callback': 'read_capacity',
         'timer_callback': 'timer_capacity',
         'data': [],
         'cnt': 0},
      'battery/charge':
        {'type'    : Float32, 
         'callback': 'read_charge',
         'timer_callback': 'timer_capacity',
         'data': [],
         'cnt': 0},
      'battery/charge_ratio':
        {'type'    : Float32, 
         'callback': 'read_charge_ratio',
         'timer_callback': 'timer_charge_ratio',
         'data': [],
         'cnt': 0},
#      'battery/charging_state':
#        {'type'    : ChargingState, 
#         'callback': 'read_charging_state',
#         'timer_callback': 'timer_charging_state',
#         'data': [],
#         'cnt': 0},
      'battery/current':
        {'type'    : Float32,
         'callback': 'read_current',
         'timer_callback': 'timer_current',
         'data': [],
         'cnt': 0},
      'battery/temperature':
        {'type'    : Int16, 
         'callback': 'read_temperature',
         'timer_callback': 'timer_temperature',
         'data': [],
         'cnt': 0},
      'battery/voltage':
        {'type'    : Float32,
         'callback': 'read_voltage',
         'timer_callback': 'timer_voltage',
         'data': [],
         'cnt': 0}
    }

    # Setup timer and callback
    # The timer acts upon the data, the subscriber receives it
    for topic, values in self.topics.items():
      # Temp callbacks required to avoid str type error
      temp_cb = eval("self.{0}".format(values['callback']))
      rospy.Subscriber(topic, values['type'], temp_cb)

      #timer_temp_cb = eval("self.{0}".format(values['timer_callback']))
      #timer_temp_cb_lambda = lambda x: timer_temp_cb(x, topic)
      #rospy.Timer(rospy.Duration(self.duration), timer_temp_cb_lambda)


  # Helper functions
  # Connection string starts with a slash
  def trim_topic(self, topic):
    if (topic[0] == "/"):
      topic = topic[1:]
    return topic


  # Sensor reading callbacks
  def read_capacity(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_charge(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_charge_ratio(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_charging_state(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_current(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_temperature(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)
  def read_voltage(self, data):
    topic = self.trim_topic(data._connection_header['topic'])

    if (len(self.topics[topic]['data']) == 5):
      print(topic, average(self.topics[topic]['data']))
      self.topics[topic]['data'] = []
    else:
      self.topics[topic]['data'].append(data.data)

  # Timer callback (averages/acts upon data)
  def timer_capacity(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_charge(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_charge_ratio(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_charging_state(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_current(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_temperature(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
  def timer_voltage(self, data, topic):
    if (len(self.topics[topic]['data']) >= 5):
      print(topic, self.topics[topic]['data'])
      self.topics[topic]['data'] = []
