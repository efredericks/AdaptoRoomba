import rospy
import sys
from std_msgs.msg import Float32


class CreateData():
  def __init__(self):
    self.bumper = None
    self.capacity = None
    self.charge = None
    self.charge_ratio = None
    self.charging_state = None
    self.current = None
    self.temperature = None




def callback(data):
    rospy.loginfo("Rx: {0}".format(data.data))
    sys.exit()

def listener():
    rospy.init_node("node1")
    rospy.Subscriber("battery/charge_ratio", Float32, callback)
    rospy.spin()

listener()

