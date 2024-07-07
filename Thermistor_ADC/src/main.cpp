#include <Arduino.h>

unsigned int c  = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  int val = analogRead(A3);
  float voltage = val *  (5.0 / 1023.0);
  Serial.print("Value: ");
  Serial.print(val, 5);
  Serial.print("\n");
  Serial.print("Volt: ");
  Serial.print(voltage, 5);
  Serial.print("\n");
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
// -> 0*c : 12102
// ->100*c: 2420
// 
}
