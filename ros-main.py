import rospy
from battery import BatteryMonitor

if __name__ == "__main__":
  rospy.init_node("create_handler")

  # Instantiate sensors
  duration = 1.0/100.0 # timer
  battery = BatteryMonitor(duration)

  # ROS loop
  rospy.spin()

