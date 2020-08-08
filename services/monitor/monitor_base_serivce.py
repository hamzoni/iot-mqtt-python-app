from datetime import datetime, timedelta

import pymongo


class MonitorBaseService:
    def __init__(self, collection):
        self.collection = collection

    def filter(self, board_name):
        p_ts = datetime.utcnow() - timedelta(seconds=60)
        p_ts = datetime.timestamp(p_ts)
        p_ts = round(p_ts)

        conditions = {
            'created_at': {
                '$gt': p_ts
            },
            'board_name': board_name
        }

        items = self.collection.find(conditions)\
            .sort([('created_at', pymongo.DESCENDING)])\
            .limit(60)

        results = []

        for item in items:
            item['_id'] = str(item['_id'])
            results.append(item)

        return {
            'results': results
        }

    def list_all(self):
        items = self.collection.find().sort([('created_at', pymongo.DESCENDING)])

        results = []

        for item in items:
            item['_id'] = str(item['_id'])
            results.append(item)

        return {
            'results': results
        }

    def clean_up(self):
        self.collection.remove()

        return {
            'results': 'success'
        }

    def insert(self, board_name: str, value: str):
        created_at = datetime.timestamp(datetime.utcnow())
        created_at = round(created_at)

        item = {
            'board_name': board_name,
            'value': value,
            'created_at': created_at
        }

        self.collection.insert_one(item)
        item['_id'] = str(item['_id'])

        return item
