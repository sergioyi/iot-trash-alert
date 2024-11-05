import paho.mqtt.client as mqtt
import psycopg2
from datetime import datetime

# Configurações do broker MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "unisales/mqtt/1"

# Configurações do banco de dados PostgreSQL
db_host = "localhost"
db_name = "lixo"
db_user = "root"
db_password = "admin"
db_port = "5432"

# Função para conexão com o banco de dados
def connect_to_db():
    return psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )

# Função que será chamada quando uma mensagem for recebida
def on_message(client, userdata, message):
    print(f"Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")
    
    # Conectar ao banco de dados e armazenar o valor
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Inserir o valor booleano True na tabela `mensagem`
        query = "INSERT INTO mensagem (mensagem, created_at) VALUES (%s, %s);"
        cursor.execute(query, (True, datetime.now()))
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        cursor.close()
        conn.close()
        print("Mensagem salva no banco de dados.")
    
    except Exception as e:
        print(f"Erro ao salvar no banco de dados: {e}")

# Criação do cliente MQTT
client = mqtt.Client()

# Definindo a função que será chamada quando uma mensagem for recebida
client.on_message = on_message

# Conectando ao broker e inscrevendo-se no tópico
client.connect(broker, port)
client.subscribe(topic)

# Mantendo o cliente ativo para ouvir as mensagens
client.loop_forever()
