# AdaptoRoomba

*Work in progress*

Experimenting with adding self-adaptive features to a Roomba platform.

## Test Experiment

Don't forget to bring up ROS:
  `roslaunch create_bringup create_2.launch`

Power test

1. Run Roomba <x> times for <y> minutes and report final battery level
2. Add testing topic and continuous testing
3. Re-run (1) and compare

Control task -- see goal model

1. Control Roomba via webcam and QR codes
2. Attempt to **go home** as the goal
3. Adapt to unanticipated scenarios - implement MAPE-K feedback loop
