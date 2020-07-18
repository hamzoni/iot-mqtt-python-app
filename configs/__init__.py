import os


def get_env(key: str, default_value: str):
    return os.environ.get(key, default_value)


class Configs:
    DB_HOST = get_env('DB_HOST', 'localhost')
    DB_USERNAME = get_env('DB_USERNAME', 'root')
    DB_PASSWORD = get_env('DB_PASSWORD', 'root1234')

    MQTT_HOST = get_env('MQTT_HOST', 'localhost')
    MQTT_PORT = get_env('MQTT_PORT', '1883')


class QueueTopics:
    ADD_TEMPERATURE = 'ADD_TEMPERATURE'


topics_registry = [
    QueueTopics.ADD_TEMPERATURE,
]
