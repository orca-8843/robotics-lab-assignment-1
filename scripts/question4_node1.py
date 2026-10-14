#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Node 1 received: %s", msg.data)

rospy.init_node('aaron')
pub = rospy.Publisher('hello_class', String, queue_size=10)
rospy.Subscriber('welcome', String, callback)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish("Hello RAA 26_28 !")
    rospy.loginfo("Node 1 published: Hello RAA 26_28 !")
    rate.sleep()