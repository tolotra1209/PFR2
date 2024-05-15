#include <AFMotor.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(0, 1); // RX, TX
#define Broche_Echo_Avant A0 // Broche Echo du HC-SR04 sur A0 AVANT
#define Broche_Trigger_Avant A1 // Broche Trigger du HC-SR04 sur A1 
#define Broche_Echo_Gauche A5 // Broche Echo du HC-SR04 sur A5 GAUCHE
#define Broche_Trigger_Gauche A4 // Broche Trigger du HC-SR04 sur A4
#define Broche_Echo_Droit A3 // Broche Echo du HC-SR04 sur A3 DROITE
#define Broche_Trigger_Droit A2 // Broche Trigger du HC-SR04 sur A2

const int distanceCible = 25; // Seuil de distance à partir duquel le robot s'arrête (en cm)

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

// Fonction pour mesurer la distance avec un capteur ultrasonore
long mesurerDistance(int triggerPin, int echoPin) {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  long Duree = pulseIn(echoPin, HIGH);
  long Distance = Duree * 0.034 / 2;
  return Distance;
}

void setSpeed(int vitesseGauche, int vitesseDroit) {
  motor1.setSpeed(vitesseGauche);
  motor2.setSpeed(vitesseDroit);
  motor3.setSpeed(vitesseDroit);
  motor4.setSpeed(vitesseGauche);
}

void avancer(int vitesseGauche, int vitesseDroit){
  setSpeed(vitesseGauche, vitesseDroit);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  
  // Continuer à avancer tant qu'aucun obstacle n'est détecté à moins de 30 cm
  while (true) {
    long distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    if (distanceAvant <= 40) {
      arreter(); // Arrêter les moteurs si un obstacle est détecté à moins de 30 cm
      break; // Sortir de la boucle
    }
    delay(50); // Attendre un court instant avant de mesurer à nouveau la distance
  }
}

void reculer(int vitesseGauche, int vitesseDroit, int temps){
  arreter(); // Arrêter les moteurs d'abord
  setSpeed(vitesseGauche, vitesseDroit);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  delay(temps);
  arreter();
}

void arreter(){
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(200);
}

void turnLeft() {
  arreter(); // Arrêter les moteurs d'abord
  setSpeed(242, 242);
  
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
  delay(600); // Ajuster au besoin
  arreter();
}

void turnRight() {
  arreter(); // Arrêter les moteurs d'abord
  setSpeed(242, 242);
  
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
  delay(600); // Ajuster au besoin
  arreter();
}

void suivreMurGauche(){
  long distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  float erreurGauche = distanceGauche - distanceCible;
  
  // Vérifier si la distance mesurée est nulle ou très grande
  if (distanceGauche != 0 && distanceGauche < 400 ) {
    // Arrêter les moteurs si un mur est détecté à moins de 40 cm
    if (distanceGauche <= 40) {
      arreter();
      return; // Sortir de la fonction
    }
    
    // Calculer les vitesses des moteurs en fonction de l'erreur
    float vitesseGauche, vitesseDroit;
    
    if (erreurGauche < 0) {
      vitesseGauche = 225;
      vitesseDroit = 100;
      avancer(vitesseGauche, vitesseDroit);
    } else if (erreurGauche > 0) {
      vitesseGauche = 100;
      vitesseDroit = 225;
      avancer(vitesseGauche, vitesseDroit);
    } else {
      vitesseGauche = 200;
      vitesseDroit = 200;
      avancer(vitesseGauche, vitesseDroit);
    }
  }
}

void suivreMurDroit(){
  long distanceDroit = mesurerDistance(Broche_Trigger_Droit, Broche_Echo_Droit);
  float erreurDroit = distanceDroit - distanceCible;
  
  // Vérifier si la distance mesurée est nulle ou très grande
  if (distanceDroit != 0 && distanceDroit < 400 ) {
    // Arrêter les moteurs si un mur est détecté à moins de 40 cm
    if (distanceDroit <= 40) {
      arreter();
      return; // Sortir de la fonction
    }
    
    // Calculer les vitesses des moteurs en fonction de l'erreur
    float vitesseGauche, vitesseDroit;
    
    if (erreurDroit > 0) {
      vitesseGauche = 225;
      vitesseDroit = 100;
      avancer(vitesseGauche, vitesseDroit);
    } else if (erreurDroit < 0) {
      vitesseGauche = 100;
      vitesseDroit = 225;
      avancer(vitesseGauche, vitesseDroit);
    } else {
      vitesseGauche = 200;
      vitesseDroit = 200;
      avancer(vitesseGauche, vitesseDroit);
    }
  }
}

void setup() {
  bluetoothSerial.begin(9600);  // Définit le débit en bauds de votre module Bluetooth.
  pinMode(Broche_Trigger_Avant, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Avant, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Gauche, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Gauche, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Droit, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Droit, INPUT); // Broche Echo en entrée
  Serial.begin(115200); // Initialisation de la communication série
  
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
  if (bluetoothSerial.available() > 0) {
    char command = bluetoothSerial.read();
    executeCommand(command);
  }
}

void executeCommand(char cmd) {
  if (cmd == 'f') {
    avancer(150, 150);
  } else if (cmd == 'b') {
    reculer(150, 150, 500); // Augmenté le temps de recul à 500 ms
  } else if (cmd == 'l') {
    turnLeft();
  } else if (cmd == 'r') {
    turnRight();
  } else if (cmd == 's') {
    arreter();
  } else if (cmd == 'a') {
    modeAuto();
  }
}

void modeAuto(){
  long distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
  long distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  long distanceDroite = mesurerDistance(Broche_Trigger_Droit, Broche_Echo_Droit);
  
  if (distanceDroite <= distanceGauche){
    reculer(200, 200, 200);
    turnLeft();
    while (distanceAvant > distanceCible) {
      suivreMurDroit();
      distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    }
  } else {
    reculer(200, 200, 200);
    turnRight();
    while (distanceAvant > distanceCible) {
      suivreMurGauche();
      distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    }
  }
  arreter(); // Arrêter les moteurs à la fin du mode automatique
}
