from services.database import DatabaseService
from services.monitor.temperature_monitor_service import TemperatureMonitorService
from services.signal.pin_control_service import PinControlService
from services.signal.pin_registry_service import PinRegistryService


class Container:
    __instance__ = None

    @classmethod
    def container(cls):
        if cls.__instance__ is None:
            cls.__instance__ = cls()
        return cls.__instance__


class DatabaseContainer(Container):
    @staticmethod
    def get_pin_collection():
        return DatabaseService.pin()

    @staticmethod
    def get_temperature_collection():
        return DatabaseService.temperature()


class ServiceContainer(Container):
    @staticmethod
    def get_temperature_monitor_service():
        return TemperatureMonitorService()

    @staticmethod
    def get_pin_registry_service():
        return PinRegistryService()

    @staticmethod
    def get_pin_control_service():
        return PinControlService()
