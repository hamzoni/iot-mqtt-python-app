from services.signal.entities.Pin import DigitalStatus


class PinControlService:

    @staticmethod
    def on(collection, board_name: str, pin_name: str):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }

        value = str(DigitalStatus.ON.value[0])
        collection.update(
            query,
            {'$set': {'digital_value': value}}
        )
        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def off(collection, board_name: str, pin_name: str):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }

        value = str(DigitalStatus.OFF.value[0])
        collection.update(
            query, {'$set': {'digital_value': value}}
        )
        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def set_value(collection, board_name: str, pin_name: str, value: float):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }
        collection.update(
            query, {'$set': {'analog_value': value}}
        )
        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def find(collection, board_name: str, pin_name: str):
        result = collection.find_one({
            'board_name': board_name,
            'pin_name': pin_name,
        })
        result['_id'] = str(result['_id'])
        return result
