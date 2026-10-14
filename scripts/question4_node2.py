#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Node 2 received: %s", msg.data)
    pub_welcome.publish("Hello Aaron Welcome !")
    pub_college.publish("Hello CET!")

rospy.init_node('SP2026')

pub_welcome = rospy.Publisher('welcome', String, queue_size=10)
pub_college = rospy.Publisher('hello_college', String, queue_size=10)
rospy.Subscriber('hello_class', String, callback)

rospy.spin()