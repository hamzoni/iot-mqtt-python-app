import pymongo
from services.signal.entities import Pin

from services.database import DatabaseService


class PinRegistryService:

    @staticmethod
    def list_all():
        collection = DatabaseService.pin()
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
    def add(record: Pin):
        collection = DatabaseService.pin()
        result = collection.insert_one({
            'pin_name': record.pin_name,
            'board_name': record.board_name,
            'type': record.type,
            'analog_value': record.analog_value,
            'digital_value': record.digital_value,
        })
        return result.acknowledged

    @staticmethod
    def remove(board_name: str, pin_name: str):
        collection = DatabaseService.pin()
        result = collection.delete_many({
            'board_name': board_name,
            'pin_name': pin_name,
        })
        return result.raw_result
