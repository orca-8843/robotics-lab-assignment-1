
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import BatteryState

def main():
    rospy.init_node('factory_data_logger_bot')

    temp_pub = rospy.Publisher(
        '/ambient_temperature', Float32, queue_size=10)
    battery_pub = rospy.Publisher(
        '/battery_state', BatteryState, queue_size=10)

    rate = rospy.Rate(4)
    last_temp = rospy.Time.now()

    while not rospy.is_shutdown():
        now = rospy.Time.now()

        if (now - last_temp).to_sec() >= 1.0:
            temp = Float32()
            temp.data = 28.5
            temp_pub.publish(temp)
            rospy.loginfo("Temperature: %.1f C", temp.data)
            last_temp = now

        battery = BatteryState()
        battery.voltage = 12.4
        battery.temperature = 30.0
        battery.percentage = 0.85
        battery.location = "Main Battery"
        battery.serial_number = "BAT-001"

        battery_pub.publish(battery)
        rospy.loginfo(
            "Battery: %.1f V | %.1f C | %.0f%% | %s | %s",
            battery.voltage, battery.temperature,
            battery.percentage * 100,
            battery.location, battery.serial_number)

        rate.sleep()

if __name__ == '__main__':
    main()
