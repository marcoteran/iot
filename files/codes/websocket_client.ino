#include <WiFi.h>
#include <WebSocketsClient.h>
#include <DHT.h>

// define the WiFi and WebSocket server details
const char* ssid = "your-ssid";
const char* password = "your-password";
const char* webSocketServerAddress = "ws://raspberry-pi-ip-address:port/";

// define the DHT11 sensor pin
#define DHTPIN 14

// initialize the DHT11 sensor
DHT dht(DHTPIN, DHT11);

// initialize the WiFi and WebSocket clients
WiFiClient wifiClient;
WebSocketsClient webSocketClient;

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  // handle WebSocket events here
}

void setup() {
  // start the serial communication
  Serial.begin(115200);

  // connect to the WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // connect to the WebSocket server
  webSocketClient.begin(webSocketServerAddress);
  webSocketClient.onEvent(webSocketEvent);

  // initialize the DHT11 sensor
  dht.begin();
}

void loop() {
  // read sensor data
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // send sensor data to the WebSocket server
  String message = String("{\"temperature\":") + temperature + String(",\"humidity\":") + humidity + String("}");
  webSocketClient.sendTXT(message);

  // wait for 5 seconds before sending the next message
  delay(5000);
}
