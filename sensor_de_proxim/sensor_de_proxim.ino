// SENSOR DE PROXIMIDADE COM ENVIO DE MENSAGEM MQTT
#include <WiFi.h>
#include <PubSubClient.h>

// Definições do sensor ultrassônico e pino LED
const int PINO_TRIG = 14;
const int PINO_ECHO = 12;
const long TEMPO_PROX_LEITURA = 500;

// Configurações de Wi-Fi
const char* ssid = "AndroidAP849C";
const char* password = "sergioluan123";

// Configurações do broker MQTT
const char* mqtt_server = "test.mosquitto.org";
WiFiClient espClient;
PubSubClient client(espClient);

void setupWiFi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando-se à rede Wi-Fi: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("Conectado! Endereço IP: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Tentando conexão MQTT...");
    if (client.connect("ArduinoClient")) {
      Serial.println("Conectado ao MQTT");
    } else {
      Serial.print("Falha na conexão, código de erro: ");
      Serial.println(client.state());
      delay(8000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setupWiFi();
  client.setServer(mqtt_server, 1883);

  pinMode(PINO_TRIG, OUTPUT);
  pinMode(PINO_ECHO, INPUT);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Leitura do sensor de proximidade
  digitalWrite(PINO_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PINO_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PINO_TRIG, LOW);

  long duracao = pulseIn(PINO_ECHO, HIGH);
  float distancia = (duracao * 0.0343) / 2;

  if (distancia < 3) {
    String message = "A lixeira está cheia!";
    client.publish("unisales/mqtt/1", message.c_str());
    Serial.println("Mensagem enviada: " + message);
    
    // Aguarda um pouco para evitar enviar mensagens continuamente
    delay(3000);
  }

  delay(TEMPO_PROX_LEITURA);
}
