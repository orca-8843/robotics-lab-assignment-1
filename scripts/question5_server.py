#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import BatteryState


def temperature_callback(msg):
    rospy.loginfo("Server temperature: %.1f C", msg.data)


def battery_callback(msg):
    rospy.loginfo(
        "Server battery: %.1f V | %.1f C | %.0f%% | %s | %s",
        msg.voltage,
        msg.temperature,
        msg.percentage * 100,
        msg.location,
        msg.serial_number
    )


def main():
    rospy.init_node('factory_data_logger_server')

    rospy.Subscriber(
        '/ambient_temperature', Float32, temperature_callback
    )
    rospy.Subscriber(
        '/battery_state', BatteryState, battery_callback
    )

    rospy.loginfo("Remote server started")
    rospy.spin()


if __name__ == '__main__':
    main()
