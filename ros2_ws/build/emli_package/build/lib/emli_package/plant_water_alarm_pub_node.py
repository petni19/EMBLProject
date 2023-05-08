#!/usr/bin/env python3
import serial
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16

class SensorReader:
    def __init__(self, port='/dev/serial/by-id/usb-MicroPython_Board_in_FS_mode_e66118c4e3695422-if00', baudrate=115200, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def read_sensor(self):
        data = self.ser.readline().decode('utf-8').strip()
        return data
    
class PlantWaterAlarmPublisher(Node):
    def __init__(self):
        super().__init__('plant_water_alarm_publisher')
        self.publisher_ = self.create_publisher(Int16, 'emli_plant_water_alarm', 10)
        self.sensor_reader = SensorReader()

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        sensor_data = self.sensor_reader.read_sensor()
        sensor_data_list = sensor_data.split(",")
        plant_water_alarm = int(sensor_data_list[0])

        msg = Int16()
        msg.data = plant_water_alarm

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)        

def main(args=None):
    rclpy.init(args=args)

    sensor_plant_water_alarm = PlantWaterAlarmPublisher()

    rclpy.spin(sensor_plant_water_alarm)

    sensor_plant_water_alarm.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
	main()            