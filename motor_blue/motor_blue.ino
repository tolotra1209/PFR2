#include <AFMotor.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(9, 10); // RX, TX

#define Broche_Echo A0 // Broche Echo du HC-SR04 sur A0
#define Broche_Trigger A1 // Broche Trigger du HC-SR04 sur A1

#define Distance_seuil 20 // Seuil de distance à partir duquel le robot s'arrête (en cm)

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

int MesureMaxi = 300; // Distance maxi a mesurer
int MesureMini = 3; // Distance mini a mesurer
long Duree;
long Distance;

void setup() {
  bluetoothSerial.begin(9600);  // Définit le débit en bauds de votre module Bluetooth.
  pinMode(Broche_Trigger, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo, INPUT); // Broche Echo en entree
  Serial.begin(9600);
}

void loop() {
  if (bluetoothSerial.available() > 0) {
    char command = bluetoothSerial.read();
    executeCommand(command);
  }
}

void executeCommand(char cmd) {
  // Mesure de la distance
  digitalWrite(Broche_Trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(Broche_Trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(Broche_Trigger, LOW);
  Duree = pulseIn(Broche_Echo, HIGH);
  Distance = Duree * 0.034 / 2;

  // Contrôle des moteurs en fonction de la distance
  if (Distance <= Distance_seuil) {
    // Arrêter les moteurs si un mur est détecté
    motor1.setSpeed(0);
    motor1.run(RELEASE);
    motor2.setSpeed(0);
    motor2.run(RELEASE);
    motor3.setSpeed(0);
    motor3.run(RELEASE);
    motor4.setSpeed(0);
    motor4.run(RELEASE);
  } else {
    switch (cmd) {
      case 'f':
        forward();
        break;
      case 'b':
        backward();
        break;
      case 'l':
        turnLeft();
        break;
      case 'r':
        turnRight();
        break;
      case 's':
        stopMotors();
        break;
    }
  }
}

void forward() {
  motor1.setSpeed(200);
  motor1.run(FORWARD);
  motor2.setSpeed(200);
  motor2.run(BACKWARD);
  motor3.setSpeed(200);
  motor3.run(FORWARD);
  motor4.setSpeed(200);
  motor4.run(BACKWARD);
}

void backward() {
  motor1.setSpeed(200);
  motor1.run(BACKWARD);
  motor2.setSpeed(200);
  motor2.run(FORWARD);
  motor3.setSpeed(200);
  motor3.run(BACKWARD);
  motor4.setSpeed(200);
  motor4.run(FORWARD);
}

void turnLeft() {
  motor1.setSpeed(0);
  motor1.run(BACKWARD);
  motor2.setSpeed(200);
  motor2.run(BACKWARD);
  motor3.setSpeed(200);
  motor3.run(FORWARD);
  motor4.setSpeed(0);
  motor4.run(FORWARD);
}

void turnRight() {
  motor1.setSpeed(200);
  motor1.run(FORWARD);
  motor2.setSpeed(0);
  motor2.run(FORWARD);
  motor3.setSpeed(0);
  motor3.run(BACKWARD);
  motor4.setSpeed(200);
  motor4.run(FORWARD);
}

void stopMotors() {
  motor1.setSpeed(0);
  motor1.run(RELEASE);
  motor2.setSpeed(0);
  motor2.run(RELEASE);
  motor3.setSpeed(0);
  motor3.run(RELEASE);
  motor4.setSpeed(0);
  motor4.run(RELEASE);
}
