#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def main():
    rospy.init_node('namespace_bot_pub')

    pub = rospy.Publisher('Greetings', String, queue_size=10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        message = String()
        message.data = "Hello!"

        pub.publish(message)
        rospy.loginfo("Published: %s", message.data)

        rate.sleep()


if __name__ == '__main__':
    main()
