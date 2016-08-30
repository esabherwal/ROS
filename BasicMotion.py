#!/usr/bin/env python
import rospy

#The velocity command message
from geometry_msgs.msg import Twist

if __name__ == ‘__main__’:
	rospy.init_node(‘move’)

	#A publisher for the move data
	pub = rospy.Publisher(‘cmd_vel_mux/input/teleop’, Twist)

	#Drive forward at a given speed. 
	command = Twist()
	command.linear.x = 0.1
	command.linear.y = 0.0
	command.linear.z = 0.0
	command.angular.x = 0.0
	command.angular.y = 0.0
	command.angular.z = 0.0

	#Loop at 10Hz, publishing movement commands until shut down.
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(command)
		rate.sleep()
