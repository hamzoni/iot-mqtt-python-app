import time
from datetime import datetime, timedelta

import pymongo


class MonitorBaseService:
    def __init__(self, collection):
        self.collection = collection

    def filter(self):
        p_ts = datetime.utcnow() - timedelta(seconds=15)
        p_ts = datetime.timestamp(p_ts)
        p_ts = round(p_ts)

        items = self.collection.find({
            'created_at': {
                '$gt': p_ts
            }
        }).sort([('created_at', pymongo.DESCENDING)]).limit(60)

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

    def insert(self, value: str):
        created_at = round(time.time())

        item = {
            'value': value,
            'created_at': created_at
        }

        self.collection.insert_one(item)
        item['_id'] = str(item['_id'])

        return item
