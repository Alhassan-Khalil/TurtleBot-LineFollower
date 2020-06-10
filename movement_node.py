#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Int32
global move_cmd

cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
def callback(steering):
    if steering.data == 2:
        left_cmd = Twist()
        left_cmd.linear.x = 0.1
        left_cmd.angular.z = 0.1
        cmd_vel.publish(left_cmd)
        rospy.sleep(0.01)
        print(steering.data)

    elif steering.data == 3:
        right_cmd = Twist()
        right_cmd.linear.x = 0.1
        right_cmd.angular.z = -0.1
        cmd_vel.publish(right_cmd)
        rospy.sleep(0.01)
        print(steering.data)
    elif steering.data == 1:
        move_cmd = Twist()
        move_cmd.linear.x = 0.15
        move_cmd.angular.z= 0
        cmd_vel.publish(move_cmd)
        rospy.sleep(0.01)
        print(steering.data)
    elif steering.data == 0:
        search_cmd = Twist()
        search_cmd.linear.x = 0.0
        search_cmd.angular.z = 0.25
        cmd_vel.publish(search_cmd)
        rospy.sleep(0.01)
        print(steering.data)


def movement():
    rospy.init_node('movement', anonymous=True)
    r = rospy.Rate(10) #10hz
    rospy.Subscriber('/vision_node', Int32, callback)
    rospy.spin()
    #move_cmd = Twist()
    #move_cmd.linear.x = 0
    #move_cmd.angular.z = 2

    #while not rospy.is_shutdown():
        #cmd_vel.publish(move_cmd)
        #callback()
        #r.sleep()


if __name__ == '__main__':
    try:
        movement()
    except rospy.ROSInterruptException: pass
