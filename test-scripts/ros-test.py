# https://bitbucket.org/reinka/blog/src/master/docker_ros_tf/scripts/talker.py

"""
battery/capacity	
The estimated charge capacity of the robot's battery (Ah)	
std_msgs/Float32

battery/charge	
The current charge of the robot's battery (Ah)	
std_msgs/Float32

battery/charge_ratio	
Charge / capacity	
std_msgs/Float32

battery/charging_state	
The charging state of the battery	
create_msgs/ChargingState

battery/current	
Current flowing through the robot's battery (A). Positive current implies charging	
std_msgs/Float32

battery/temperature	
The temperature of the robot's battery (degrees Celsius)	
std_msgs/Int16

battery/voltage	
Voltage of the robot's battery (V)	
std_msgs/Float32

bumper	
Bumper state message (including light sensors on bumpers)	
create_msgs/Bumper

wheeldrop	
At least one of the drive wheels has dropped	
std_msgs/Empty


odom	
Robot odometry according to wheel encoders	
nav_msgs/Odometry

"""



import rospy
from std_msgs.msg import String, Bool, Empty

def callback(data):
    rospy.loginfo("I heard {0}".format(data.data))

def talker():
  init = True
  pub = rospy.Publisher('debris_led', Bool, queue_size=10)
  pub2 = rospy.Publisher('dock', Empty, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)

  cnt = 0 
  while not rospy.is_shutdown():
    #pub.publish(init)
    #rate.sleep()
    #if (init == True):
    #  init = False
    #else:
    #  init = True
#
#    cnt+=1
#    if cnt > 10:
#      pub2.publish()
      break
      
    #rospy.loginfo()

if __name__ == "__main__":
  try:
    talker()
  except rospy.ROSInterruptException as e:
    print("Error: {0}".format(e))
