#!/usr/bin/env python3

import rospy
from std_srvs.srv import Trigger, TriggerResponse


def battery_callback(request):
    battery_info = (
        "Voltage: 12.4 V | "
        "Temperature: 30.0 C | "
        "Battery: 85% | "
        "Location: Main Battery | "
        "Serial Number: BAT-001"
    )

    rospy.loginfo("Battery information requested")
    rospy.loginfo(battery_info)

    return TriggerResponse(
        success=True,
        message=battery_info
    )


def main():
    rospy.init_node('factory_battery_service_bot')

    rospy.Service(
        '/get_battery_info',
        Trigger,
        battery_callback
    )

    rospy.loginfo("Battery service is ready")
    rospy.spin()


if __name__ == '__main__':
    main()