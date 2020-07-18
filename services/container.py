from services.monitor.temperature_monitor_service import TemperatureMonitorService


class Container:
    __instance__ = None

    @classmethod
    def container(cls):
        if cls.__instance__ is None:
            cls.__instance__ = cls()
        return cls.__instance__


class ServiceContainer(Container):
    @staticmethod
    def get_temperature_monitor_service():
        return TemperatureMonitorService()
