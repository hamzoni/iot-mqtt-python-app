import json

from services.configs import QueueTopics
from services.queues.models.queue_signal_message import QueueSignalMessage
from services.queues.queue_publish_service import QueuePublishService
from services.signal.entities.Pin import DigitalStatus


class PinControlService:

    @staticmethod
    def on(collection, board_name: str, pin_name: str):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }

        value = str(DigitalStatus.ON.value[0])

        # store to database
        result = collection.update(
            query,
            {'$set': {'digital_value': value}}
        )

        # publish queue message
        if result['n'] > 0:
            message = QueueSignalMessage(
                board_name=board_name,
                pin_name=pin_name,
                value=value,
            )
            message = json.dumps(message.__dict__)
            _topic = f'{board_name}_{QueueTopics.SET_SIGNAL_ON}'
            QueuePublishService.publish(_topic, message)

        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def off(collection, board_name: str, pin_name: str):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }

        # store to database
        value = str(DigitalStatus.OFF.value[0])
        result = collection.update(
            query, {'$set': {'digital_value': value}}
        )

        # publish queue message
        if result['n'] > 0:
            message = QueueSignalMessage(
                board_name=board_name,
                pin_name=pin_name,
                value=value,
            )
            message = json.dumps(message.__dict__)
            _topic = f'{board_name}_{QueueTopics.SET_SIGNAL_OFF}'
            QueuePublishService.publish(_topic, message)

        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def set_value(collection, board_name: str, pin_name: str, value: float):
        query = {
            'board_name': board_name,
            'pin_name': pin_name,
        }

        # store to database
        result = collection.update(
            query, {'$set': {'analog_value': value}}
        )

        # publish queue message
        if result['n'] > 0:
            message = QueueSignalMessage(
                board_name=board_name,
                pin_name=pin_name,
                value=str(value),
            )
            message = json.dumps(message.__dict__)
            _topic = f'{board_name}_{QueueTopics.SET_SIGNAL_VALUE}'
            QueuePublishService.publish(_topic, message)

        return PinControlService.find(collection, board_name, pin_name)

    @staticmethod
    def find(collection, board_name: str, pin_name: str):
        result = collection.find_one({
            'board_name': board_name,
            'pin_name': pin_name,
        })
        if result:
            result['_id'] = str(result['_id'])
        return result
