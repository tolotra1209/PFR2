#include "AFMotor.h"

// Création des objets pour les moteurs
AF_DCMotor motor1(1);//BAS GAUCHE
AF_DCMotor motor2(2);//HAUT GAUCHE
AF_DCMotor motor3(3);//BAS DROITE
AF_DCMotor motor4(4);//HAUT DROITE

void setup() {
  // Configuration de la vitesse initiale et de l'état des moteurs
  motor1.setSpeed(255);
  motor1.run(RELEASE);
  motor2.setSpeed(255);
  motor2.run(RELEASE);
  motor3.setSpeed(255);
  motor3.run(RELEASE);
  motor4.setSpeed(255);
  motor4.run(RELEASE);
}

void loop() {

  //avancer 
  motor1.setSpeed(120);  // Réduire la vitesse du moteur 1 (gauche)
  motor2.setSpeed(120);  // Augmenter la vitesse du moteur 2 (droite)
  motor3.setSpeed(120);  // Augmenter la vitesse du moteur 3 (droite)
  motor4.setSpeed(120);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  delay(1000);
  
  // Tourner à gauche
  motor1.setSpeed(0);  // Réduire la vitesse du moteur 1 (gauche)
  motor2.setSpeed(255);  // Augmenter la vitesse du moteur 2 (droite)
  motor3.setSpeed(255);  // Augmenter la vitesse du moteur 3 (droite)
  motor4.setSpeed(0);  // Réduire la vitesse du moteur 4 (gauche)
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
  delay(2000);

  //avancer
  motor1.setSpeed(120);  // Réduire la vitesse du moteur 1 (gauche)
  motor2.setSpeed(120);  // Augmenter la vitesse du moteur 2 (droite)
  motor3.setSpeed(120);  // Augmenter la vitesse du moteur 3 (droite)
  motor4.setSpeed(120);  
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  delay(1000);// Attendre 2 secondes

  // Tourner à droite
  motor1.setSpeed(255);  // Augmenter la vitesse du moteur 1 (gauche)
  motor2.setSpeed(0);  // Réduire la vitesse du moteur 2 (droite)
  motor3.setSpeed(0);  // Réduire la vitesse du moteur 3 (droite)
  motor4.setSpeed(255);  // Augmenter la vitesse du moteur 4 (gauche)
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
  delay(2000);           // Attendre 2 secondes

  // Arrêter les moteurs
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(1000);           // Attendre 1 seconde avant de recommencer
}
