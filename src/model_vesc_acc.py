#! /usr/bin/python
import rospy
import subprocess, os, signal

from std_msgs.msg import Float64


def dutycyclePublisher():
    rospy.init_node('model_vesc_acc_node')

    pub_steer = rospy.Publisher("commands/servo/position",Float64, queue_size = 100)
    pub_throttle = rospy.Publisher("commands/motor/duty_cycle", Float64, queue_size = 100)
    pub_speed = rospy.Publisher("commands/motor/speed", Float64, queue_size = 100)


    rate1 = rospy.Rate(2)

    rate = rospy.Rate(10)

    steering_angle = 0.5
    rospy.loginfo(steering_angle)
    pub_steer.publish(steering_angle)

    count = 0
    count_max = 8 #determines increse in duty cycle

    duty_cycle_inc = 0.05
    duty_cycle = 0

    command = "rosbag record commands/servo/position commands/motor/duty_cycle commands/motor/speed /vrpn_client_node/f110car_2/pose"
    rosbag_process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)


    rospy.loginfo("intializing")


    rate1.sleep()
    rate1.sleep()

    rospy.loginfo("starting")

    while not rospy.is_shutdown() and count < count_max:

        rospy.loginfo(duty_cycle)
        pub_throttle.publish(duty_cycle)

        duty_cycle = (duty_cycle -  duty_cycle_inc)*-1
        count = count + 1

        rate.sleep()

    terminate_process_and_children(rosbag_process)

    rospy.loginfo("speed = 0")
    pub_speed.publish(0)

    rospy.loginfo("termianting")

def terminate_process_and_children(p):
  import psutil
  process = psutil.Process(p.pid)
  for sub_process in process.children(recursive=True):
      sub_process.send_signal(signal.SIGINT)
  p.wait()  # we wait for children to terminate
  #p.terminate()





if __name__=='__main__':
    try:
        dutycyclePublisher()
    except rospy.ROSInterruptException:
        pass
