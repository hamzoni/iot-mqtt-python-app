from services.containers.base_container import BaseContainer
from services.database import DatabaseService


class DatabaseContainer(BaseContainer):
    @staticmethod
    def get_pin_collection():
        return DatabaseService.pin()
