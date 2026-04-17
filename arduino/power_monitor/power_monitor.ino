const int voltagePin = A0;
const int currentPin = A1;
const int tempPin = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int voltageRaw = analogRead(voltagePin);
  int currentRaw = analogRead(currentPin);
  int tempRaw = analogRead(tempPin);

  float voltage = (voltageRaw / 1023.0) * 25.0;
  float current = ((currentRaw / 1023.0) * 5.0 - 2.5) / 0.185;
  float temperature = (tempRaw * 5.0 * 100.0) / 1023.0;

  Serial.print(voltage);
  Serial.print(',');
  Serial.print(current);
  Serial.print(',');
  Serial.println(temperature);

  delay(2000);
}