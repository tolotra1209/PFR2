#include <AFMotor.h>
#include <SoftwareSerial.h>

#define Broche_Echo_Avant A0 // Broche Echo du HC-SR04 sur A0 AVANT
#define Broche_Trigger_Avant A1 // Broche Trigger du HC-SR04 sur A1 
#define Broche_Echo_Gauche A5 // Broche Echo du HC-SR04 sur A5 GAUCHE
#define Broche_Trigger_Gauche A4 // Broche Trigger du HC-SR04 sur A4
#define Broche_Echo_Droit A3 // Broche Echo du HC-SR04 sur A3 DROITE
#define Broche_Trigger_Droit A2 // Broche Trigger du HC-SR04 sur A2

SoftwareSerial bluetoothSerial(9, 10); // RX, TX

const int distanceCible = 15; // Distance cible par rapport aux murs (en cm)
const float coefficientProportionnel = 20; // Coefficient proportionnel pour le régulateur de distance

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() {
  pinMode(Broche_Trigger_Avant, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Avant, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Gauche, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Gauche, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Droit, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Droit, INPUT); // Broche Echo en entrée

  Serial.begin(115200); // Initialisation de la communication série
}

// Fonction pour mesurer la distance avec un capteur ultrasonore
long mesurerDistance(int triggerPin, int echoPin) {
  digitalWrite(triggerPin, LOW);
  digitalWrite(triggerPin, HIGH);
  digitalWrite(triggerPin, LOW);
  long Duree = pulseIn(echoPin, HIGH);
  long Distance = Duree * 0.034 / 2;
  return Distance;
}

// Fonction pour réguler la distance par rapport au mur gauche et ajuster la vitesse des moteurs
void regulerDistanceMurGauche(float vitesseGauche, float vitesseDroit) {
  // Limiter les vitesses pour éviter les valeurs extrêmes
  vitesseGauche = constrain(vitesseGauche, 0, 255);
  vitesseDroit = constrain(vitesseDroit, 0, 255);

  // Appliquer les vitesses aux moteurs
  motor1.setSpeed(vitesseGauche);
  motor2.setSpeed(vitesseGauche);
  motor3.setSpeed(vitesseDroit);
  motor4.setSpeed(vitesseDroit);

  // Faire avancer les moteurs dans la direction appropriée
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
}

void loop() {
  // Mesurer la distance avec le capteur avant
  long distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
  // Mesurer la distance avec le capteur droit
  long distanceDroit = mesurerDistance(Broche_Trigger_Droit, Broche_Echo_Droit);
  // Mesurer la distance avec le capteur gauche
  long distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  float erreurGauche = distanceCible - distanceGauche;
  Serial.println(erreurGauche);
  // Vérifier si la distance mesurée est nulle
  if (distanceGauche != 0) {
    // Afficher les distances mesurées
    //Serial.print("Distance avant : ");
    //Serial.print(distanceAvant);
    //Serial.print(" cm, Distance droit : ");
    //Serial.print(distanceDroit);
    //Serial.print(" cm, Distance gauche : ");
    //Serial.print(distanceGauche);
    //Serial.println(" cm");
    
    // Calculer les vitesses des moteurs en fonction de l'erreur
    float vitesseGauche, vitesseDroit;
    
    if (erreurGauche > 0) {
      
      vitesseGauche = 200;
      vitesseDroit = 0;
      motor1.setSpeed(vitesseGauche);
      motor2.setSpeed(vitesseGauche);
      motor3.setSpeed(vitesseDroit);
      motor4.setSpeed(vitesseDroit);
    
      // Faire avancer les moteurs dans la direction appropriée
      motor1.run(FORWARD);
      motor2.run(BACKWARD);
      motor3.run(FORWARD);
      motor4.run(BACKWARD);
      delayMicroseconds(100);
      motor1.run(RELEASE);
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
      delayMicroseconds(100);
    }
    if (erreurGauche < 0) {
      
      vitesseGauche = 0;
      vitesseDroit = 200;
      motor1.setSpeed(vitesseGauche);
      motor2.setSpeed(vitesseGauche);
      motor3.setSpeed(vitesseDroit);
      motor4.setSpeed(vitesseDroit);
    
      // Faire avancer les moteurs dans la direction appropriée
      motor1.run(FORWARD);
      motor2.run(BACKWARD);
      motor3.run(FORWARD);
      motor4.run(BACKWARD);
    } else {
    
      // Faire avancer les moteurs dans la direction appropriée
    motor1.run(RELEASE);
    motor2.run(RELEASE);
    motor3.run(RELEASE);
    motor4.run(RELEASE);
    }
  } else {
    // Passer à la prochaine itération de la boucle sans exécuter le reste du code
    motor1.run(RELEASE);
    motor2.run(RELEASE);
    motor3.run(RELEASE);
    motor4.run(RELEASE);
    delayMicroseconds(100);
    return;
  }
}
