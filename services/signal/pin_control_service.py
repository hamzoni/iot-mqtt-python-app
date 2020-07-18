from services.signal.entities.Pin import DigitalStatus


class PinControlService:

    @staticmethod
    def on(collection, board_name: str, pin_name: str):
        return collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'digital_value': DigitalStatus.ON.value}}
        )

    @staticmethod
    def off(collection, board_name: str, pin_name: str):
        collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'digital_value': DigitalStatus.OFF.value}}
        )

    @staticmethod
    def set_value(collection, board_name: str, pin_name: str, value: float):
        return collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'analog_value': value}}
        )

    @staticmethod
    def find(collection, board_name: str, pin_name: str):
        return collection.find_one({
            'board_name': board_name,
            'pin_name': pin_name,
        })
