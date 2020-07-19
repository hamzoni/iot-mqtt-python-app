import json


class QueueSignalMessage:
    board_name: str
    pin_name: str
    value: str

    def __init__(self, board_name: str, pin_name: str, value: str):
        self.board_name = board_name
        self.pin_name = pin_name
        self.value = value

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
