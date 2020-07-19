import paho.mqtt.client as mqtt

from services.configs import Configs


class QueuePublishService:
    @staticmethod
    def publish(topic: str, payload: str):
        client = mqtt.Client()
        client.connect(Configs.MQTT_HOST, int(Configs.MQTT_PORT), 60)
        print(f'Publish message to {topic} with payload {payload}')
        client.publish(topic, payload)
        client.disconnect()
