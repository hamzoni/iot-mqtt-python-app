from services.database import DatabaseService
from services.monitor.monitor_base_serivce import MonitorBaseService


class TemperatureMonitorService(MonitorBaseService):

    def __init__(self):
        collection = DatabaseService.temperature()
        super(MonitorBaseService, self).__init__(collection)
