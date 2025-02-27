from dynamixel_sdk import *
from serial import SerialException
from typing import Any
from math import pi
from dataclasses import dataclass


PROTOCOL_VERSION = 2
# Control table addresses for XL330-M288-T

# EEPROM REGISTER ADDRESSES - Permanently stored in memory once changed

ADDR_XL330_MODEL_NUMBER = 0
ADDR_XL330_MODEL_INFORMATION = 2
ADDR_XL330_FIRMWARE_VERSION = 6
ADDR_XL330_PRESENT_POSITION = 132

# RAM registers
ADDR_XL330_TORQUE_ENABLE = 64
ADDR_XL330_GOAL_POSITION = 116


class XL330Comm:

    def __init__(self, port: str = None, baudrate: int = 57600):

        self.port = port
        self.baudrate = baudrate
        self.port_handler = PortHandler(port)
        self.packet_handler = PacketHandler(PROTOCOL_VERSION)

        self.servo_ids: list = [int]
        self.servos: list = [int]
        self.total_servos: int = 0


        try:
            self.open_port()
        except SerialException as e:
            print(e)
            quit()
        else:
            print(f"Succeeded to open port {self.port}")

        try:
            self.set_baud_rate()
        except SerialException as e:
            print(e)
            quit()
        else:
            print(f"Succeeded to set baudrate: {self.baudrate}")

    def open_port(self):
        self.port_handler.openPort()

    def close_port(self):
        self.port_handler.closePort()

    def set_baud_rate(self):
        self.port_handler.setBaudRate(baudrate=self.baudrate)

    def add_servo(self, servo):
        self.servos.append(servo)
        self.servo_ids.append(servo.servo_id)
        servo.set_comm(self.port_handler, self.packet_handler)
        self.total_servos += 1

    # def torque_enabled(self, is_enabled:bool = False):
    #     self.packet_handler.write1ByteTxRx(self.port_handler, BROADCAST_ID, ADDR_XL330_TORQUE_ENABLE, is_enabled)


class XL330Ctrl:

    def __init__(self, servo_id):
        self.servo_id = servo_id
        self.port_handler = None
        self.packet_handler = None
        self.goal_pos = None

    def set_comm(self, servo_port_handler, servo_packet_handler) -> None:
        self.port_handler = servo_port_handler
        self.packet_handler = servo_packet_handler

    def torque_enabled(self, is_enabled: bool = False) -> None:
        dxl_comm_result, dxl_error = self.packet_handler.write1ByteTxRx(self.port_handler, self.servo_id,
                                                                        ADDR_XL330_TORQUE_ENABLE, is_enabled)

        self.print_comm_error_result(dxl_comm_result, dxl_error)
        print(f"Torque enabled for servo with id {self.servo_id} is set to: {is_enabled}")

    def get_position(self, radian: bool = False) -> float:
        reg_data, dxl_comm_result, dxl_error = self.packet_handler.read4ByteTxRx(self.port_handler, self.servo_id,
                                                                                 ADDR_XL330_PRESENT_POSITION)
        self.print_comm_error_result(dxl_comm_result, dxl_error)

        if radian:
            angle = pi*float(reg_data)/2048.0
        else:
            angle = 180*float(reg_data)/2048.0
        return angle

    def _set_goal_pos(self, angle: float, radian: bool = False) -> None:
        if radian:
            self.goal_pos = int(2048.0*angle/pi)
            pass
        else:
            self.goal_pos = int(2048.0*angle/180)

    def set_position(self, goal_pos, radian=False) -> None:

        self._set_goal_pos(angle=goal_pos, radian=radian)
        dxl_comm_result, dxl_error = self.packet_handler.write4ByteTxRx(self.port_handler, self.servo_id,
                                                                        ADDR_XL330_GOAL_POSITION, self.goal_pos)
        self.print_comm_error_result(dxl_comm_result, dxl_error)

    def print_comm_error_result(self, comm_result: Any, error: Any) -> None:
        if comm_result != COMM_SUCCESS:
            print(f"\n{self.packet_handler.getTxRxResult(comm_result)}")
            print("Please check the following:\n"
                  "Is the motor connected and powered?\n"
                  "Is the correct servo_id entered?\n")
            quit()
        elif error != 0:
            print(f"{self.packet_handler.getRxPacketError(error)}")
            quit()
