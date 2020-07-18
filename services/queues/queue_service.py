import threading

import paho.mqtt.client as mqtt

from services.configs import topics_registry, Configs
from services.queues.queue_route_service import QueueRouteService


class QueueService:
    client: any

    def __init__(self):
        def on_connect(_client, user_data, flags, rc):
            for topic in topics_registry:
                _client.subscribe(topic)

        def on_message(_client, user_data, message):
            content = message.payload.decode('utf-8')
            QueueRouteService.resolve_message(message.topic, content)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        self.client = client

    def start(self):
        self.client.connect(Configs.MQTT_HOST, int(Configs.MQTT_PORT), 60)
        self.client.loop_forever()

    @staticmethod
    def run():
        service = QueueService()

        t1 = threading.Thread(target=service.start)
        t1.daemon = True
        t1.start()
