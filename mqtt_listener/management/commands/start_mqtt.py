from django.core.management.base import BaseCommand
from mqtt_listener.mqtt_client import start_mqtt_client

class Command(BaseCommand):
    help = 'Inicia o cliente MQTT'

    def handle(self, *args, **kwargs):
        start_mqtt_client()
