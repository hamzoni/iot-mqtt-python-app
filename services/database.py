import pymongo

from ..configs import Configs


class DatabaseService:
    db: any

    def __init__(self):
        db_uri = f'mongodb://{Configs.DB_USERNAME}:{Configs.DB_PASSWORD}@{Configs.DB_HOST}:27017'
        db = pymongo.MongoClient(db_uri)

        self.db = db['fsb']  # database

    @staticmethod
    def temperature():
        service = DatabaseService()
        return service.db['temperature']  # temperature monitoring collection
