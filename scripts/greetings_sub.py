#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo("Received message: %s", message.data)

def greetings_subscriber():
    rospy.init_node('RAA26_subnode', anonymous=False)

    rospy.Subscriber('/Greetings', String, callback)

    rospy.loginfo("Subscriber is listening to /Greetings")
    rospy.spin()

if __name__ == '__main__':
    try:
        greetings_subscriber()
    except rospy.ROSInterruptException:
        pass
