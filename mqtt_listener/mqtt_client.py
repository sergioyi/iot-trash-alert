import paho.mqtt.client as mqtt
import psycopg2
from datetime import datetime
from django.conf import settings

# Configurações do broker MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "unisales/mqtt/1"

# Função que será chamada quando uma mensagem for recebida
def on_message(client, userdata, message):
    print(f"Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")
    try:
        # Conectando ao banco de dados Django
        from mqtt_listener.models import Mensagem
        Mensagem.objects.create(mensagem=True)
        print("Mensagem salva no banco de dados Django.")
    except Exception as e:
        print(f"Erro ao salvar no banco de dados: {e}")

def start_mqtt_client():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    print("Cliente MQTT iniciado. Aguardando mensagens...")
    client.loop_forever()
