#!/usr/bin/env python3

import sys
import rospy
from std_msgs.msg import String

def greetings_publisher():
    node_name = sys.argv[1] if len(sys.argv) > 1 else 'aaron_pubnode'

    rospy.init_node(node_name, anonymous=False)
    pub = rospy.Publisher('Greetings', String, queue_size=10)
    rate = rospy.Rate(10)

    message = "Hello, I am Aaron"

    while not rospy.is_shutdown():
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        greetings_publisher()
    except rospy.ROSInterruptException:
        pass
