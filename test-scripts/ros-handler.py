import rospy
import sys
from std_msgs.msg import Float32, Int16, Empty, UInt16, Bool, UInt8MultiArray
from create_msgs.msg import ChargingState, Bumper, Mode, DefineSong, PlaySong
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


# topics/subscribers c/o https://github.com/AutonomyLab/create_robot
class CreateHandler():
  def __init__(self):
    self.topics = {
      'battery/capacity':       Float32,
      'battery/charge':         Float32,
      'battery/charge_ratio':   Float32,
      'battery/charging_state': ChargingState,
      'battery/current':        Float32,
      'battery/temperature':    Int16,
      'battery/voltage':        Float32,
      'bumper':                 Bumper,
      'clean_button':           Empty,
      'day_button':             Empty,
      'hour_button':            Empty,
      'minute_button':          Empty,
      'dock_button':            Empty,
      'spot_button':            Empty,
      'ir_omni':                UInt16,
      'joint_states':           JointState,
      'mode':                   Mode,
      'odom':                   Odometry,
      'wheeldrop':              Empty
    }

    # Setup rx flags and subscribers based on topic name
    self.topic_states = {}
    self.subscribers  = {}
    for topic,topic_type in self.topics.items():
      self.topic_states[topic] = False
      self.subscribers = rospy.Subscriber(topic, topic_type, self.callback)

    self.subscribers = {
      'cmd_vel':     Twist,
      'debris_led':  Bool,
      'spot_led':    Bool,
      'dock_led':    Bool,
      'check_led':   Bool,
      'power_led':   Bool,
      'dock':        Empty,
      'undock':      Empty,
      'define_song': DefineSong,
      'play_song':   PlaySong
      #'set_ascii': UInt8MultiArray, -- not on my create
    }


    self.bumper = None
    self.capacity = None
    self.charge = None
    self.charge_ratio = None
    self.charging_state = None
    self.current = None
    self.temperature = None


  def callback(self, data):
    rospy.loginfo("Rx: {0}".format(data))




def callback(data):
    rospy.loginfo("Rx: {0}".format(data.data))
    sys.exit()

def listener():
    rospy.init_node("node1")
    rospy.Subscriber("battery/charge_ratio", Float32, callback)
    rospy.spin()

if __name__ == "__main__":
  rospy.init_node("Create Handler")
  robot = CreateHandler()
  rospy.spin()
