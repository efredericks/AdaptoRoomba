import rospy
import argparse
from battery import BatteryMonitor
import math

from std_msgs.msg import Float32, Int16, Empty
from geometry_msgs.msg import Twist

vel_msg = Twist()

# Write out data and safely shutdown ROS
def end_experiment(event=None):
  elapsed_time = rospy.get_time() - start_time
  print("Experiment complete - [{0}] seconds.".format(str(elapsed_time)))
  #print(battery.topics)
  rospy.signal_shutdown("done")

def update_path(event=None):
  global path_index, pathTimer, pathPublisher, vel_msg
  elapsed_time = rospy.get_time() - start_time

  vel_msg.linear.x = 0
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = 0

  # command forward
  if (paths[path_index] == 'forward'):
    vel_msg.linear.x = 0.1
    print("moving forward at [{0}] seconds".format(str(elapsed_time)))
    #vel_msg.angular.z = 5.0 * 2 * math.pi / 360.
    #pathPublisher.publish(vel_msg)


  # command reverse
  elif (paths[path_index] == 'reverse'):
    vel_msg.linear.x = -0.1
    print("moving backward at [{0}] seconds".format(str(elapsed_time)))
    #vel_msg.angular.z = 0
    #pathPublisher.publish(vel_msg)
  # command spin
  elif (paths[path_index] == 'spin'):
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 1.57/2.0
    print("riding spinners at [{0}] seconds".format(str(elapsed_time)))
    #vel_msg.angular.z = 0
    #pathPublisher.publish(vel_msg)
  else:
    assert "Error"

  path_index += 1
  if (path_index > len(paths)-1):
    pathTimer.shutdown()

parser = argparse.ArgumentParser(description="ROS continuous testing experimental framework")
parser.add_argument("--expr", default="baseline", help="baseline | test")
parser.add_argument("--runtime", default=60, help="seconds to run", type=float)
parser.add_argument("--verbose", action='store_true', help="print debugging information")

# Instantiate robot/sensors
rospy.init_node("create_handler")
start_time = rospy.get_time()

duration = 1.0/100.0 # timer
battery = BatteryMonitor(duration)

path_index = 0
paths = ['forward', 'reverse', 'spin']

args = parser.parse_args()

if args.verbose:
  print("Running experiment [{0}] for [{1}] seconds.".format(args.expr, args.runtime))

# Set timers (shutdown, update steps)
endTimer = rospy.Timer(rospy.Duration(args.runtime), end_experiment, oneshot=True)
pathTimer = rospy.Timer(rospy.Duration(args.runtime/(len(paths)+1)), update_path)

# Publishers
pathPublisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
dockPublisher = rospy.Publisher("/undock", Empty, queue_size=10)

rate = rospy.Rate(5.0)
#dockPublisher.publish()
#pathPublisher.publish(vel_msg)

# ROS loop
#rospy.spin()

while not rospy.is_shutdown():
  pathPublisher.publish(vel_msg)
  rate.sleep()
  


  

#if __name__ == "__main__":
