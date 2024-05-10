#include <AFMotor.h>
#include <SoftwareSerial.h>

#define Broche_Echo_Avant A0 // Broche Echo du HC-SR04 sur A0 AVANT
#define Broche_Trigger_Avant A1 // Broche Trigger du HC-SR04 sur A1 
#define Broche_Echo_Gauche A5 // Broche Echo du HC-SR04 sur A5 GAUCHE
#define Broche_Trigger_Gauche A4 // Broche Trigger du HC-SR04 sur A4
#define Broche_Echo_Droit A3 // Broche Echo du HC-SR04 sur A3 DROITE
#define Broche_Trigger_Droit A2 // Broche Trigger du HC-SR04 sur A2

SoftwareSerial bluetoothSerial(9, 10); // RX, TX

const int distanceCible = 20; // Distance cible par rapport aux murs (en cm)

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
  delay(200);
  relacher();
}

void reculer(int vitesseGauche, int vitesseDroit, int temps){
  setSpeed(vitesseGauche, vitesseDroit);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  delay(temps);
  relacher();
}

void relacher(){
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(200);
}

void turnLeft() {
  setSpeed(242, 242);
  
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
  delay(570); // Adjust as needed
  relacher();
}

void turnRight() {
  setSpeed(242, 242);
  
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
  delay(570); // Adjust as needed
  relacher();
}

void suivreMurGauche(){
  long distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  float erreurGauche = distanceGauche - distanceCible;
  // Serial.println(erreurGauche);
  
  // Vérifier si la distance mesurée est nulle ou très grande
  if (distanceGauche != 0 && distanceGauche < 400 ) {
    // Calculer les vitesses des moteurs en fonction de l'erreur
    float vitesseGauche, vitesseDroit;
    
    if (erreurGauche < 0) {
      vitesseGauche = 200;
      vitesseDroit = 100;
      avancer(vitesseGauche, vitesseDroit);
    } else if (erreurGauche > 0) {
      vitesseGauche = 100;
      vitesseDroit = 200;
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
  // Serial.println(erreurDroit);
  
  // Vérifier si la distance mesurée est nulle ou très grande
  if (distanceDroit != 0 && distanceDroit < 400 ) {
    // Calculer les vitesses des moteurs en fonction de l'erreur
    float vitesseGauche, vitesseDroit;
    
    if (erreurDroit > 0) {
      vitesseGauche = 200;
      vitesseDroit = 100;
      avancer(vitesseGauche, vitesseDroit);
    } else if (erreurDroit < 0) {
      vitesseGauche = 100;
      vitesseDroit = 200;
      avancer(vitesseGauche, vitesseDroit);
    } else {
      vitesseGauche = 200;
      vitesseDroit = 200;
      avancer(vitesseGauche, vitesseDroit);
    }
  }
}

void setup() {
  pinMode(Broche_Trigger_Avant, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Avant, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Gauche, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Gauche, INPUT); // Broche Echo en entrée
  pinMode(Broche_Trigger_Droit, OUTPUT); // Broche Trigger en sortie
  pinMode(Broche_Echo_Droit, INPUT); // Broche Echo en entrée

  Serial.begin(115200); // Initialisation de la communication série
  long distanceAvant = 0;
  long distanceDroit = 600;
  long distanceGauche = 0;

  // Mesurer la distance avec le capteur avant
  distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
  if (distanceAvant == 0){
    distanceAvant == distanceAvant+400;
  }
  // Mesurer la distance avec le capteur droit
  distanceDroit = 600;
  if (distanceDroit == 0){
    distanceDroit == distanceDroit+400;
  }
  // Mesurer la distance avec le capteur gauche
  distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  if (distanceGauche == 0){
    distanceGauche == distanceGauche+400;
  }
  if ((distanceGauche <= distanceDroit) && (distanceGauche <= distanceAvant)){
    turnLeft();
  } else if (distanceDroit <= distanceAvant){
    turnRight();
  }

  while (distanceAvant == 0){
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
  }
  
  while (distanceAvant > distanceCible) {
    avancer(150, 150);
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
  }

  reculer(100, 100, 10);
  relacher(); // Arrêter les moteurs lorsque la distance cible est atteinte
}

void loop() {

  // Avancer tant que la distance avant est supérieure à la distance cible
  long distanceAvant = 0;
  long distanceGauche = 0;
  long distanceDroite = 600;
  
  while (distanceGauche == 0){
    distanceGauche = mesurerDistance(Broche_Trigger_Gauche, Broche_Echo_Gauche);
  }

  while (distanceDroite == 0){
    distanceDroite = mesurerDistance(Broche_Trigger_Droit, Broche_Echo_Droit);
  }

  if (distanceDroite <= distanceGauche){
    turnLeft();
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    while (distanceAvant > distanceCible) {
    suivreMurDroit();
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    }
  } else {
    turnRight();
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    while (distanceAvant > distanceCible) {
    suivreMurGauche();
    distanceAvant = mesurerDistance(Broche_Trigger_Avant, Broche_Echo_Avant);
    }
  }
}
