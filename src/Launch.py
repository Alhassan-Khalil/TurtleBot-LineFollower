#!/bin/bash
#!/usr/bin/python

#run this file by using terminal (  "python Launch.py"  )

import os
import time
from subprocess import call,Popen

#copying the ground plane to gazebo file 

orginal_location = os.getcwd()
os.chdir('../Gazebo_map') 
old_dir = os.getcwd()
print "Copying from directory %s" % old_dir
os.system('cp -r my_ground_plane ~/.gazebo/models/')
print " Done"
#--------------------------------------------------

#going back to the file location
os.chdir(orginal_location)
#launching the map 
Popen(['xterm', '-e', 'roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=/home/default/TurtleBot-LineFollower/Gazebo_map/test_map5.world'])

time.sleep(5)

#starting the vision node
Popen(['xterm', '-e', 'python vision_node.py'])
time.sleep(5)
#launch the movemnt 
Popen(['xterm', '-e', 'python movement_node.py'])

