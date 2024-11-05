from flask import Flask, request, jsonify # type: ignore
import paho.mqtt.client as mqtt # type: ignore
import time

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "unisales/mqtt/1"

mqttc = mqtt.Client()

mqttc.connect(MQTT_BROKER, MQTT_PORT, 60)

mqttc.loop_start()

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"status": "erro", "mensagem": "Nenhum dado enviado"}), 400

    try:
        message = str(data)
        msg_info = mqttc.publish(MQTT_TOPIC, message, qos=1)
        msg_info.wait_for_publish()  
        return jsonify({"status": "sucesso", "mensagem": "Dados enviados ao broker MQTT"}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)