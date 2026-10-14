
#!/usr/bin/env python3

import rospy
from std_srvs.srv import Trigger


def main():
    rospy.init_node('factory_battery_service_client')

    rospy.loginfo("Remote server waiting for battery service...")
    rospy.wait_for_service('/get_battery_info')

    try:
        get_battery = rospy.ServiceProxy('/get_battery_info', Trigger)

        rospy.loginfo("Requesting battery information before patrol")
        response = get_battery()

        if response.success:
            rospy.loginfo("Battery information received:")
            rospy.loginfo(response.message)
            rospy.loginfo("Bot is ready for patrol")
        else:
            rospy.logwarn("Battery information request failed")

    except rospy.ServiceException as error:
        rospy.logerr("Service call failed: %s", error)
        return

    rospy.loginfo("Client remains running for graph inspection")
    rospy.spin()


if __name__ == '__main__':
    main()

