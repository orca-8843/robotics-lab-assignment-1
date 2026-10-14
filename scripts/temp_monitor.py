#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, String


def temperature_callback(msg):
    temperature = msg.data

    if temperature > 40.0:
        rospy.logwarn("High temperature: %.1f C", temperature)
        alarm_pub.publish(String(data="High Temperature Detected!"))
    else:
        rospy.loginfo("Temperature is safe: %.1f C", temperature)


def main():
    global alarm_pub

    rospy.init_node('temp_monitor')

    alarm_pub = rospy.Publisher('/factory_alarm', String, queue_size=10)
    rospy.Subscriber('/factory_temp', Float32, temperature_callback)

    rospy.loginfo("Temperature monitor started")
    rospy.spin()


if __name__ == '__main__':
    main()
