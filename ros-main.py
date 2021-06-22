import rospy
import argparse
from battery import BatteryMonitor
#import time

parser = argparse.ArgumentParser(description="ROS continuous testing experimental framework")
parser.add_argument("--expr", default="baseline", help="baseline | test")
parser.add_argument("--runtime", default=60, help="seconds to run", type=float)
parser.add_argument("--verbose", action='store_true', help="print debugging information")

# Instantiate robot/sensors
rospy.init_node("create_handler")
start_time = rospy.get_time()

duration = 1.0/100.0 # timer
battery = BatteryMonitor(duration)

def end_experiment(event=None):
  elapsed_time = rospy.get_time() - start_time
  print("Experiment complete - [{0}] seconds.".format(str(elapsed_time)))
  #print(battery.topics)
  rospy.signal_shutdown("done")


if __name__ == "__main__":
  args = parser.parse_args()

  if args.verbose:
    print("Running experiment [{0}] for [{1}] seconds.".format(args.expr, args.runtime))

  rospy.Timer(rospy.Duration(args.runtime), end_experiment, oneshot=True)

  # ROS loop
  rospy.spin()
