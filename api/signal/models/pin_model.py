from typing import Optional

from pydantic import BaseModel


class Pin(BaseModel):
    pin_name: Optional[str]
    board_name: Optional[str]  # name of the machine of the pin
    type: Optional[str]
    analog_value: Optional[float]  # for analog pin only
    digital_value: Optional[int]  # for digital pin only
