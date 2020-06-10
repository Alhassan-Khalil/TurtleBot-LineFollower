#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from math import radians
from std_msgs.msg import Int32


cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
def callback(steering):
	# Twist is a datatype for velocity
	forword_cmd = Twist()
	# let's go forward at 0.2 m/s
	forword_cmd.linear.x = 0.2
	
	left_cmd = Twist()
	left_cmd.linear.x = 0.1
	left_cmd.angular.z = radians(45); #45 deg/s in radians/s

	right_cmd = Twist()
	right_cmd.linear.x = 0.1
	right_cmd.angular.z = radians(-45); #45 deg/s in radians/s

	Search_cmd = Twist()
	Search_cmd.linear.x = 0
	Search_cmd.angular.z = radians(-45); #45 deg/s in radians/s
#-----------------------------------------------------------------------------

	if steering.data == 1:
		# publish the velocity
		cmd_vel.publish(forword_cmd)
		rospy.sleep(0.01)
		rospy.loginfo("Straight")
	elif steering.data== 2:
		cmd_vel.publish(left_cmd)
		rospy.sleep(0.01)
		rospy.loginfo("Left")
	elif steering.data== 3:
		cmd_vel.publish(right_cmd)
		rospy.sleep(0.01)
		rospy.loginfo("right")
	elif steering.data== 0:
		cmd_vel.publish(Search_cmd)
		rospy.sleep(0.01)
		rospy.loginfo("search")


def movement():
	rospy.init_node('movement', anonymous=True)
	steering = rospy.Subscriber("/vision_node",Int32,callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		movement()
	except rospy.ROSInterruptException: pass
