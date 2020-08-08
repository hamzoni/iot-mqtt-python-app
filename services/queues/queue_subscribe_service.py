import threading

import paho.mqtt.client as mqtt

from services.configs import topics_registry, Configs, QueueTopics
from services.containers.database_container import DatabaseContainer
from services.containers.service_container import ServiceContainer
from services.signal.pin_registry_service import PinRegistryService


class QueueSubscribeService:
    client: any

    def __init__(self):
        def on_connect(_client, user_data, flags, rc):
            # get all board in databases
            db = DatabaseContainer.get_pin_collection()
            service = PinRegistryService()
            board_names = service.list_all_boards(db)

            for topic in topics_registry:
                print(f'Register topic {topic}')
                for board_name in board_names:
                    _topic = f'{board_name}_{topic}'
                    _client.subscribe(_topic)

        def on_message(_client, user_data, message):
            content = message.payload.decode('utf-8')
            QueueSubscribeService.resolve_message(message.topic, content)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        self.client = client

    @staticmethod
    def resolve_message(topic: str, message: str):
        # print(f'Receiving message with Topic {topic} - Message {message}')

        if QueueTopics.TEMPERATURE_CHANGE in topic:
            board_name = topic.replace(f'_{QueueTopics.TEMPERATURE_CHANGE}', '')
            service = ServiceContainer.get_temperature_monitor_service()
            service.insert(board_name, message)
        elif QueueTopics.MOISTURE_CHANGE in topic:
            board_name = topic.replace(f'_{QueueTopics.MOISTURE_CHANGE}', '')
            service = ServiceContainer.get_moisture_monitor_service()
            service.insert(board_name, message)

    def start(self):
        self.client.connect(Configs.MQTT_HOST, int(Configs.MQTT_PORT), 60)
        self.client.loop_forever()

    @staticmethod
    def run():
        service = QueueSubscribeService()

        t1 = threading.Thread(target=service.start)
        t1.daemon = True
        t1.start()

        return service
