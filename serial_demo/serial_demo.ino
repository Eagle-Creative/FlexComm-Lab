/*
 * FlexComm-Lab Arduino Serial Test Handler
 * ----------------------------------------
 * This script demonstrates basic serial communication with FlexComm-compatible systems.
 * It receives simple text commands and responds with JSON-formatted messages, suitable
 * for integration and testing with the FlexComm framework.
 *
 * Supported Commands:
 *   - GET_SENSOR : Responds with mock JSON sensor data (temperature, humidity)
 *   - PING       : Responds with a JSON 'pong' reply
 *   - HELP       : Lists available commands
 *
 * Usage:
 *   1. Upload this sketch to your Arduino (e.g., Uno, Mega, Nano).
 *   2. Open the Serial Monitor (baud rate: 115200).
 *   3. Enter one of the supported commands and press Enter.
 *   4. The Arduino will respond with a JSON-formatted reply.
 */

String inputBuffer = "";

void setup() {
  Serial.begin(115200);
  Serial.println("{\"status\": \"Arduino ready\"}");
}

void loop() {
  // Read incoming serial data into inputBuffer
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (inputBuffer.length() > 0) {
        handleCommand(inputBuffer);
        inputBuffer = "";
      }
    } else {
      inputBuffer += c;
    }
  }
}

void handleCommand(String cmd) {
  cmd.trim();
  cmd.toUpperCase();

  if (cmd == "GET_SENSOR") {
    sendMockSensorData();
  } else if (cmd == "PING") {
    Serial.println("{\"reply\": \"pong\"}");
  } else if (cmd == "HELP") {
    Serial.println("{\"commands\": [\"GET_SENSOR\", \"PING\", \"HELP\"]}");
  } else if (cmd.length() > 0) {
    Serial.print("{\"error\": \"Unknown command: ");
    Serial.print(cmd);
    Serial.println("\"}");
  }
}

void sendMockSensorData() {
  float temp = 22.5 + (random(-50, 50) / 10.0);      // Simulate temp in range 17.5–27.5°C
  float humidity = 45.0 + (random(-100, 100) / 10.0); // Simulate humidity in range 35–55%
  Serial.print("{\"temperature\": ");
  Serial.print(temp, 1);
  Serial.print(", \"humidity\": ");
  Serial.print(humidity, 1);
  Serial.println("}");
  Serial.flush();
}
