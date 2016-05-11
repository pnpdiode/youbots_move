#!/usr/bin/env python
import getch
import roslib; roslib.load_manifest('nodes')
import rospy
from std_msgs.msg import Int8
import sensor_msgs.msg
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.transformations import euler_from_quaternion
import time

def move(x,y,z):
	twist1.linear.x = x
	twist1.linear.y = y
	twist1.angular.z = z
	twist2.linear.x = x
	twist2.linear.y = y
	twist2.angular.z = z
	pub1.publish(twist1)
	pub2.publish(twist2)


twist1 = Twist()
twist2 = Twist()

rospy.init_node('nodes', anonymous=True)


#open terminal and run "rostopic list" command to see which topics are being
#published

pub1 = rospy.Publisher('youbot1/cmd_vel', Twist, queue_size=1)
pub2 = rospy.Publisher('youbot2/cmd_vel', Twist, queue_size=1)




while(1):

	move(0.5,0,0)#forward
	time.sleep(2)
	move(-0.5,0,0)#backwards
	time.sleep(2)
	move(0,0.5,0)#sideways_left
	time.sleep(2)
	move(0,-0.5,0)#sideways_right
	time.sleep(2)
	move(0,0,0.5)#rotate left
	time.sleep(2)
	move(0,0,-0.5)#rotate right
	time.sleep(2)
	move(0,0,0)#stop
	break


exit()
