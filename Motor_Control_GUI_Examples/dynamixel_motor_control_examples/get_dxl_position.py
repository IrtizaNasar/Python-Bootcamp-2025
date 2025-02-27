import time

from servos.XL330 import XL330Comm, XL330Ctrl

# Starting communication for Dynamixel servo
serial = XL330Comm(port="COM28")

# Declaring a servo object
servo1 = XL330Ctrl(servo_id=1)

# Adding servo to start communication
serial.add_servo(servo=servo1)

# Disabling torque for a single servo
servo1.torque_enabled(is_enabled=False)

try:
    while True:
        print(servo1.get_position())
        time.sleep(0.1)


except KeyboardInterrupt:
    print("Stopping program")
