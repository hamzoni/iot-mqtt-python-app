from services.containers.base_container import BaseContainer
from services.monitor.moisture_monitor_service import MoistureMonitorService
from services.monitor.temperature_monitor_service import TemperatureMonitorService
from services.signal.pin_control_service import PinControlService
from services.signal.pin_registry_service import PinRegistryService


class ServiceContainer(BaseContainer):

    @staticmethod
    def get_temperature_monitor_service():
        return TemperatureMonitorService()

    @staticmethod
    def get_moisture_monitor_service():
        return MoistureMonitorService()

    @staticmethod
    def get_pin_registry_service():
        return PinRegistryService()

    @staticmethod
    def get_pin_control_service():
        return PinControlService()
