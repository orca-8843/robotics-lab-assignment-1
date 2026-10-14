#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def main():
    rospy.init_node('robot_status_publisher')

    pub = rospy.Publisher(
        '/robot_status',
        String,
        queue_size=10,
        latch=True
    )

    rospy.sleep(1)

    pub.publish(String(data="System Ready"))
    rospy.loginfo("Published: System Ready")

    rospy.spin()


if __name__ == '__main__':
    main()
