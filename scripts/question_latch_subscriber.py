#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(message):
    rospy.loginfo("Received: %s", message.data)


def main():
    rospy.init_node('robot_status_subscriber')

    rospy.Subscriber('/robot_status', String, callback)

    rospy.loginfo("Subscriber is waiting for messages")
    rospy.spin()


if __name__ == '__main__':
    main()
