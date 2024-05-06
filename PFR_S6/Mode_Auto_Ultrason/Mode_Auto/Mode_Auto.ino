#include <AFMotor.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(9, 10); // RX, TX

#define Broche_Echo_Avant A0 // Broche Echo du HC-SR04 sur A0 AVANT
#define Broche_Trigger_Avant A1 // Broche Trigger du HC-SR04 sur A1 
#define Broche_Echo_Droit A3 // Broche Echo du HC-SR04 sur A3 DROITE
#define Broche_Trigger_Droit A2 // Broche Trigger du HC-SR04 sur A2
#define Broche_Echo_Gauche A5 // Broche Echo du HC-SR04 sur A5 GAUCHE
#define Broche_Trigger_Gauche A4 // Broche Trigger du HC-SR04 sur A4

#define Distance_seuil 10 // Seuil de distance à partir duquel le robot s'arrête (en cm)

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() {
  bluetoothSerial.begin(9600);  // Définit le débit en bauds de votre module Bluetooth.
  pinMode(Broche_Trigger_Avant, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Avant, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Droit, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Droit, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Gauche, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Gauche, INPUT); // Broche Echo en entrée
  Serial.begin(9600);
}

void loop() {
  long duration, distance;

  // Mesure obstacle frontal
  digitalWrite(Broche_Trigger_Avant, LOW);
  delayMicroseconds(2);
  digitalWrite(Broche_Trigger_Avant, HIGH);
  delayMicroseconds(10);
  digitalWrite(Broche_Trigger_Avant, LOW);
  duration = pulseIn(Broche_Echo_Avant, HIGH);
  distance = (duration / 2) / 29.1; // Conversion en cm

  if (distance < 10) { // Obstacle frontal détecté
    Serial.println("Détection obstacle frontal");
    Serial.print("Distance : ");
    Serial.print(distance);
    Serial.println(" cm !");
    Serial.println("Corriger trajectoire");

    // Mesure obstacle à droite
    digitalWrite(Broche_Trigger_Droit, LOW);
    delayMicroseconds(2);
    digitalWrite(Broche_Trigger_Droit, HIGH);
    delayMicroseconds(10);
    digitalWrite(Broche_Trigger_Droit, LOW);
    duration = pulseIn(Broche_Echo_Droit, HIGH);
    distance = (duration / 2) / 29.1;

    if (distance < Distance_seuil) {
      Serial.println("Détection obstacle à droite");
      Serial.print("Distance : ");
      Serial.print(distance);
      Serial.println(" cm !");
      Serial.println("Ne pas tourner à droite");
      delay(500);

      // Mesure obstacle à gauche
      digitalWrite(Broche_Trigger_Gauche, LOW);
      delayMicroseconds(2);
      digitalWrite(Broche_Trigger_Gauche, HIGH);
      delayMicroseconds(10);
      digitalWrite(Broche_Trigger_Gauche, LOW);
      duration = pulseIn(Broche_Echo_Gauche, HIGH);
      distance = (duration / 2) / 29.1;

      if (distance < Distance_seuil) {
        Serial.println("Détection obstacle à gauche");
        Serial.print("Distance : ");
        Serial.print(distance);
        Serial.println(" cm !");
        Serial.println("Ne pas tourner à gauche - Faire marche arrière + demi-tour");
        delay(500);

        // Faire marche arrière
        motor1.run(BACKWARD);
        motor2.run(FORWARD);
        motor3.run(BACKWARD);
        motor4.run(FORWARD);
        motor1.setSpeed(100);
        motor2.setSpeed(100);
        motor3.setSpeed(100);
        motor4.setSpeed(100);
        delay(500);

        // Faire demi-tour
        motor1.run(FORWARD);
        motor2.run(BACKWARD);
        motor3.run(BACKWARD);
        motor4.run(FORWARD);
        motor1.setSpeed(100);
        motor2.setSpeed(100);
        motor3.setSpeed(100);
        motor4.setSpeed(100);
        delay(500);
      } else {
        // Tourner à gauche
        motor1.run(BACKWARD);
        motor2.run(FORWARD);
        motor3.run(FORWARD);
        motor4.run(BACKWARD);
        motor1.setSpeed(100);
        motor2.setSpeed(100);
        motor3.setSpeed(100);
        motor4.setSpeed(100);
        delay(500);
        motor1.run(RELEASE);
        motor2.run(RELEASE);
        motor3.run(RELEASE);
        motor4.run(RELEASE);
        delay(500);
      }
    } else {
      // Tourner à droite
      motor1.run(FORWARD);
      motor2.run(BACKWARD);
      motor3.run(BACKWARD);
      motor4.run(FORWARD);
      motor1.setSpeed(100);
      motor2.setSpeed(100);
      motor3.setSpeed(100);
      motor4.setSpeed(100);
      delay(500);
      motor1.run(RELEASE);
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
      delay(500);
    }
  } else {
    // Pas d'obstacle devant, avancer
    // Mesure obstacle à droite
    digitalWrite(Broche_Trigger_Droit, LOW);
    delayMicroseconds(2);
    digitalWrite(Broche_Trigger_Droit, HIGH);
    delayMicroseconds(10);
    digitalWrite(Broche_Trigger_Droit, LOW);
    duration = pulseIn(Broche_Echo_Droit, HIGH);
    distance = (duration / 2) / 29.1;

    if (distance > 10) {
      motor2.run(BACKWARD);
      motor4.run(BACKWARD);
      motor1.run(FORWARD);
      motor3.run(FORWARD);
      motor2.setSpeed(100);
      motor4.setSpeed(100);
      motor1.setSpeed(100);
      motor3.setSpeed(100);
    } else {
      float CMG = ((4 + (distance - 7)) / 10);
      motor2.run(BACKWARD);
      motor4.run(BACKWARD);
      motor1.run(FORWARD);
      motor3.run(FORWARD);

    // Mesure obstacle à gauche
    digitalWrite(Broche_Trigger_Gauche, LOW);
    delayMicroseconds(2);
    digitalWrite(Broche_Trigger_Gauche, HIGH);
      motor2.setSpeed(100 * CMG);
      motor4.setSpeed(100 * CMG);
      motor1.setSpeed(100 * CMG);
      motor3.setSpeed(100 * CMG);
    }
    delayMicroseconds(10);
    digitalWrite(Broche_Trigger_Gauche, LOW);
    duration = pulseIn(Broche_Echo_Gauche, HIGH);
    distance = (duration / 2) / 29.1;

    if (distance > 10) {
      motor1.run(FORWARD);
      motor3.run(FORWARD);
      motor2.run(BACKWARD);
      motor4.run(BACKWARD);
      motor1.setSpeed(100);
      motor3.setSpeed(100);
      motor2.setSpeed(100);
      motor4.setSpeed(100);
    } else {
    }
  }
}
