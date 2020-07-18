from configs import QueueTopics
from services.container import ServiceContainer


class QueueRouteService:
    @staticmethod
    def resolve_message(topic: str, message: str):
        print(f'Topic: {topic}')
        print(f'Message: {message}')

        if topic == QueueTopics.ADD_TEMPERATURE:
            service = ServiceContainer.get_temperature_monitor_service()
            service.insert(message)
