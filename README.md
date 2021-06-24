# AdaptoRoomba

*Work in progress*

Experimenting with adding self-adaptive features to a Roomba platform.

## Test Experiment

Controller: Raspberry Pi 3B, running Ubuntu 18 and ROS Melodic.

Install ROS and Create2 hooks via: https://github.com/AutonomyLab/create_robot

Don't forget to bring up ROS:
  `roslaunch create_bringup create_2.launch`

Check for dock success (should be positive):
  `rostopic echo -n 1 "battery/current"`

If stuck not-charging, place on dock and command to dock:
  `rostopic pub /dock std_msgs/Empty`

### Power test

1. Run Roomba X times for Y minutes and report final battery level
2. Add testing topic and continuous testing
3. Re-run (1) and compare

### Control task -- see goal model

1. Control Roomba via webcam and QR codes
2. Attempt to **go home** as the goal
3. Adapt to unanticipated scenarios - implement MAPE-K feedback loop
