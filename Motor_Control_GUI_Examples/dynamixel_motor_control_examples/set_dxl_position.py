import time
from servos.XL330 import XL330Comm, XL330Ctrl

# Starting communication for Dynamixel servo
serial_connection = XL330Comm(port="/dev/tty.usbserial-FT6S4H67")

# Declaring a servo object
servo = XL330Ctrl(servo_id=1)

# Adding servo to start communication
serial.add_servo(servo=servo)

# Enabling torque for a single servo
# When torque is enabled this allows the motor to move freely.
servo.torque_enabled(is_enabled=True)

count_1 = 0
servo1.set_position(count_1)
time.sleep(1)

while count_1 < 359:
    count_1 += 1
    servo1.set_position(count_1)

while count_1 > 0:
    count_1 -= 1
    servo1.set_position(count_1)
