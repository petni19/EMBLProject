#!/usr/bin/env python3
import serial
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorReader:
    def __init__(self, port='/dev/serial/by-id/usb-MicroPython_Board_in_FS_mode_e66118c4e3695422-if00', baudrate=115200, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def read_sensor(self):
        data = self.ser.readline().decode('utf-8').strip()
        return data

class PlantWaterAlarmPublisher(Node):
    def __init__(self):
        super().__init__('plant_water_alarm_publisher')
        self.publisher_ = self.create_publisher(String, 'emli_plant_water_alarm', 10)
        self.sensor_reader = SensorReader()

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.sensor_reader.read_sensor()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class PumpWaterAlarmPublisher(Node):
    def __init__(self):
        super().__init__('pump_water_alarm_publisher')
        self.publisher_ = self.create_publisher(String, 'emli_pump_water_alarm', 10)
        self.sensor_reader = SensorReader()

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.sensor_reader.read_sensor()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class SoilMoisturePublisher(Node):
    def __init__(self):
        super().__init__('soil_moisture_publisher')
        self.publisher_ = self.create_publisher(String, 'emli_soil_moisture', 10)
        self.sensor_reader = SensorReader()

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.sensor_reader.read_sensor()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class AmbientLightPublisher(Node):
    def __init__(self):
        super().__init__('ambient_light_publisher')
        self.publisher_ = self.create_publisher(String, 'emli_ambient_light', 10)
        self.sensor_reader = SensorReader()

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.sensor_reader.read_sensor()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    sensor_plant_water_alarm = PlantWaterAlarmPublisher()
    sensor_pump_water_alarm = PumpWaterAlarmPublisher()
    sensor_soil_moisture = SoilMoisturePublisher()
    sensor_ambient_light = AmbientLightPublisher()

    rclpy.spin(sensor_plant_water_alarm)
    rclpy.spin(sensor_pump_water_alarm)
    rclpy.spin(sensor_soil_moisture)
    rclpy.spin(sensor_ambient_light)

    sensor_plant_water_alarm.destroy_node()
    sensor_pump_water_alarm.destroy_node()
    sensor_soil_moisture.destroy_node()
    sensor_ambient_light.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
	main()
