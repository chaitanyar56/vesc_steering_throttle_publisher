#! /usr/bin/python
import rospy

from std_msgs.msg import Float64
from random import randint

def steeringPublisher():
    rospy.init_node('test_steering')
    pub_steer = rospy.Publisher("commands/servo/position",Float64, queue_size=100)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
	rand_number = randint(0,2)
	if rand_number == 0:
	    steering_angle = 0.5
	    rospy.loginfo(steering_angle)
            pub_steer.publish(steering_angle)
	elif rand_number == 1:
	    steering_angle = 0.3
            rospy.loginfo(steering_angle)
            pub_steer.publish(steering_angle)
	else:
	    steering_angle = 0.7
            rospy.loginfo(steering_angle)
            pub_steer.publish(steering_angle)
	
	

        rate.sleep()





if __name__=='__main__':
    try:
        steeringPublisher()
    except rospy.ROSInterruptException:
	pass
