#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(message):
    rospy.loginfo("Received from Bot 1: %s", message.data)


def main():
    rospy.init_node('namespace_sub')

    rospy.Subscriber('Greetings', String, callback)

    rospy.loginfo("Subscriber listening to Bot 1")
    rospy.spin()


if __name__ == '__main__':
    main()
