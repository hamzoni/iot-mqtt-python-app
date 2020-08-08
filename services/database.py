import pymongo

from services.configs import Configs


class DatabaseService:
    db: any

    def __init__(self):
        db_uri = f'mongodb://{Configs.DB_USERNAME}:{Configs.DB_PASSWORD}@{Configs.DB_HOST}:27017'
        db = pymongo.MongoClient(db_uri)

        self.db = db['fsb']  # database

    # monitor service
    @staticmethod
    def temperature():
        # temperature monitoring collection
        service = DatabaseService()
        return service.db['temperature']

    @staticmethod
    def moisture():
        # moisture monitoring collection
        service = DatabaseService()
        return service.db['moisture']

    # signal service
    @staticmethod
    def pin():
        # pin registry collection
        service = DatabaseService()
        return service.db['pin']
