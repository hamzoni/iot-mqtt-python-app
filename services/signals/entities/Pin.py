from enum import Enum


class PinType(Enum):
    ANALOG = 0,
    DIGITAL = 1,


class DigitalStatus(Enum):
    OFF = 0,
    ON = 1,


class Pin:
    pin_name: str
    board_name: str  # name of the machine of the pin
    type: PinType
    analog_value: float  # for analog pin only
    digital_value: DigitalStatus  # for digital pin only
