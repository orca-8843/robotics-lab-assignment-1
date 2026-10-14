
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32


def main():
    rospy.init_node('temp_sensor')

    pub = rospy.Publisher('/factory_temp', Float32, queue_size=10)
    rate = rospy.Rate(2)

    temperature = 25.0
    increasing = True

    while not rospy.is_shutdown():
        msg = Float32()
        msg.data = temperature
        pub.publish(msg)

        rospy.loginfo("Temperature: %.1f C", msg.data)

        if increasing:
            temperature += 2.0
            if temperature > 55.0:
                temperature = 55.0
                increasing = False
        else:
            temperature -= 2.0
            if temperature < 25.0:
                temperature = 25.0
                increasing = True

        rate.sleep()


if __name__ == '__main__':
    main()
