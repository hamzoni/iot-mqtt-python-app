from services.database import DatabaseService
from services.monitor.monitor_base_serivce import MonitorBaseService


class MoistureMonitorService(MonitorBaseService):

    def __init__(self):
        collection = DatabaseService.moisture()
        super().__init__(collection)
