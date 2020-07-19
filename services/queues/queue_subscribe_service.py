import threading

import paho.mqtt.client as mqtt

from services.configs import topics_registry, Configs, QueueTopics
from services.containers.service_container import ServiceContainer
from services.queues.models.queue_signal_message import QueueSignalMessage


class QueueSubscribeService:
    client: any

    def __init__(self):
        def on_connect(_client, user_data, flags, rc):
            for topic in topics_registry:
                _client.subscribe(topic)

        def on_message(_client, user_data, message):
            content = message.payload.decode('utf-8')
            QueueSubscribeService.resolve_message(message.topic, content)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        self.client = client

    @staticmethod
    def resolve_message(topic: str, message: str):
        print(f'Receiving message with Topic {topic} - Message {message}')

        if topic == QueueTopics.MONITOR_ADD_TEMPERATURE:
            service = ServiceContainer.get_temperature_monitor_service()
            service.insert(message)

        elif topic == QueueTopics.SET_SIGNAL_ON:
            queue = QueueSignalMessage.from_json(message)

        elif topic == QueueTopics.SET_SIGNAL_OFF:
            queue = QueueSignalMessage.from_json(message)

        elif topic == QueueTopics.SET_SIGNAL_VALUE:
            queue = QueueSignalMessage.from_json(message)

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
