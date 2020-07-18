from services.database import DatabaseService
from services.signals.entities.Pin import DigitalStatus


class PinControlService:

    @staticmethod
    def on(board_name: str, pin_name: str):
        collection = DatabaseService.pin()
        return collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'digital_value': DigitalStatus.ON}}
        )

    @staticmethod
    def off(board_name: str, pin_name: str):
        collection = DatabaseService.pin()
        return collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'digital_value': DigitalStatus.OFF}}
        )

    @staticmethod
    def set_value(board_name: str, pin_name: str, value: float):
        collection = DatabaseService.pin()
        return collection.update(
            {
                'board_name': board_name,
                'pin_name': pin_name,
            },
            {'$set': {'analog_value': value}}
        )
