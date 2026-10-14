#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Node 3 received: %s", msg.data)

rospy.init_node('CET')
rospy.Subscriber('hello_college', String, callback)
rospy.spin()