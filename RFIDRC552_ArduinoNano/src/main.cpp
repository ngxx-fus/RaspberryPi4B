#include <Arduino.h>
#include "./MFRC522/MFRC522.h"
#include "custom_pin.h"
#include <SPI.h>

#define SS_pin  
#define RST_pin D7

MFRC522 my_rfid;

void setup(){
    pinMode(D3, OUTPUT);
}

void loop() {
    delay(999);
    digitalWrite(D3, HIGH);
    delay(1);
    digitalWrite(D3, LOW);
}

