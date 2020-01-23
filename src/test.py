#! /usr/bin/python

import rospy

from std_msgs.msg import Float64


def steeringPublisher():
    rospy.init_node('test__node')
    
    pub_steer = rospy.Publisher("commands/servo/position",Float64, queue_size = 100)
    pub_throttle = rospy.Publisher("commands/motor/duty_cycle", Float64, queue_size = 100)
    pub_speed = rospy.Publisher("commands/motor/speed", Float64, queue_size = 100)

    rate = rospy.Rate(2)
    
    steering_angle = 0.5
    
    rospy.loginfo(steering_angle)
    pub_steer.publish(steering_angle)
    
    count = 0
    count_max = 4# determines increse in duty cycle
    
    duty_cycle_inc = 0.05
    duty_cycle = 0
    
    #rospy.loginfo(duty_cycle_inc)
    #pub_throttle.publish(duty_cycle_inc)

    while not rospy.is_shutdown() and count < count_max:

        #rospy.loginfo(0.1)
        #pub_throttle.publish(1.0)

        rospy.loginfo(200)
        pub_speed.publish(2000)

        #duty_cycle = duty_cycle -  duty_cycle_inc
        count = count + 1

        rate.sleep()

    rospy.loginfo(200)
    pub_speed.publish(200)



if __name__=='__main__':
    try:
        steeringPublisher()
    except rospy.ROSInterruptException:
        pass


