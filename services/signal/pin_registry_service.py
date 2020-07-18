import pymongo

from services.signal.entities import Pin


class PinRegistryService:

    @staticmethod
    def list_all(collection):
        items = collection.find().sort([
            ('created_at', pymongo.DESCENDING)
        ])

        results = []

        for item in items:
            item['_id'] = str(item['_id'])
            results.append(item)

        return {
            'results': results
        }

    @staticmethod
    def add(collection, record: Pin):
        result = collection.insert_one({
            'pin_name': record.pin_name,
            'board_name': record.board_name,
            'type': record.type,
            'analog_value': record.analog_value,
            'digital_value': record.digital_value,
        })
        return result.acknowledged

    @staticmethod
    def remove(collection, board_name: str, pin_name: str):
        result = collection.delete_many({
            'board_name': board_name,
            'pin_name': pin_name,
        })
        return result.raw_result
