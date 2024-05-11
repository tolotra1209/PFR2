#include <SoftwareSerial.h>
#include <AFMotor.h>

// Création d'un objet de type SoftwareSerial pour communiquer avec le module Bluetooth
SoftwareSerial bluetooth(9, 10);

// Assignation des moteurs aux objets Adafruit_DCMotor
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() {
  // Initialisation de la communication série avec le module Bluetooth
  bluetooth.begin(9600);
  Serial.begin(9600); // Initialisation du moniteur série
  Serial.println("Initialisation terminée");
  
  // Initialisation des moteurs
  motor1.setSpeed(0);
  motor1.run(RELEASE);
  motor2.setSpeed(0);
  motor2.run(RELEASE);
  motor3.setSpeed(0);
  motor3.run(RELEASE);
  motor4.setSpeed(0);
  motor4.run(RELEASE);
}

void loop() {
  if (bluetooth.available() > 0) {
    char command = bluetooth.read(); // Lecture de la commande envoyée par le module Bluetooth
    Serial.print("Commande reçue : ");
    Serial.println(command);
    
    // Exécution de l'action correspondante en fonction de la commande reçue
    switch(command) {
      case 'f': // Avancer
        Serial.println("Avancer");
        forward();
        break;
      case 'b': // Reculer
        Serial.println("Reculer");
        backward();
        break;
      case 'l': // Gauche
        Serial.println("Tourner à gauche");
        turnLeft();
        break;
      case 'r': // Droite
        Serial.println("Tourner à droite");
        turnRight();
        break;
      case 's': // Arrêter
        Serial.println("Arrêter");
        stopMotors();
        break;
      default:
        Serial.println("Commande invalide");
        break;
    }
  }
}

void forward() {
  Serial.println("Moteurs en avant");
  motor1.setSpeed(200);
  motor1.run(FORWARD);
  motor2.setSpeed(200);
  motor2.run(FORWARD);
  motor3.setSpeed(200);
  motor3.run(FORWARD);
  motor4.setSpeed(200);
  motor4.run(FORWARD);
}

void backward() {
  Serial.println("Moteurs en arrière");
  motor1.setSpeed(200);
  motor1.run(BACKWARD);
  motor2.setSpeed(200);
  motor2.run(BACKWARD);
  motor3.setSpeed(200);
  motor3.run(BACKWARD);
  motor4.setSpeed(200);
  motor4.run(BACKWARD);
}

void turnLeft() {
  Serial.println("Tourner à gauche");
  motor1.setSpeed(200);
  motor1.run(BACKWARD);
  motor2.setSpeed(200);
  motor2.run(BACKWARD);
  motor3.setSpeed(200);
  motor3.run(FORWARD);
  motor4.setSpeed(200);
  motor4.run(FORWARD);
}

void turnRight() {
  Serial.println("Tourner à droite");
  motor1.setSpeed(200);
  motor1.run(FORWARD);
  motor2.setSpeed(200);
  motor2.run(FORWARD);
  motor3.setSpeed(200);
  motor3.run(BACKWARD);
  motor4.setSpeed(200);
  motor4.run(BACKWARD);
}

void stopMotors() {
  Serial.println("Arrêt des moteurs");
  motor1.setSpeed(0);
  motor1.run(RELEASE);
  motor2.setSpeed(0);
  motor2.run(RELEASE);
  motor3.setSpeed(0);
  motor3.run(RELEASE);
  motor4.setSpeed(0);
  motor4.run(RELEASE);
}
