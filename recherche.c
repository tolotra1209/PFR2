#include <Pixy2.h>
#include <PIDLoop.h>

Pixy2 pixy;
PIDLoop panLoop(400, 0, 400, true);
PIDLoop tiltLoop(500, 0, 500, true);

int panPosition = 500; // Valeur initiale médiane pour servomoteur pan
int tiltPosition = 500; // Valeur initiale médiane pour servomoteur tilt
bool searchMode = true;
unsigned long lastMoveTime = 0;
const unsigned long moveInterval = 2000; // Intervalle entre les mouvements (en millisecondes)

enum Direction {LEFT, CENTER, RIGHT};
Direction currentDirection = LEFT;

enum VerticalDirection {UP, DOWN};
VerticalDirection currentVerticalDirection = UP; // Définir la direction verticale initiale

void setup()
{
  Serial.begin(115200);
  Serial.print("Starting...\n");

  pixy.init();
  pixy.changeProg("color_connected_components");
  
  // Définir les positions initiales des servos
  pixy.setServos(panPosition, tiltPosition);
}

void loop()
{
  static int i = 0;
  int32_t panOffset, tiltOffset;

  // Obtenir les blocs actifs de Pixy
  pixy.ccc.getBlocks();

  if (pixy.ccc.numBlocks)
  {
    // Si un objet est détecté, arrêter le balayage
    searchMode = false;
    
    i++;
    if (i % 60 == 0)
      Serial.println(i);
    
    panOffset = (int32_t)pixy.frameWidth/2 - (int32_t)pixy.ccc.blocks[0].m_x;
    tiltOffset = (int32_t)pixy.ccc.blocks[0].m_y - (int32_t)pixy.frameHeight/2;

    panLoop.update(panOffset);
    tiltLoop.update(tiltOffset);

    pixy.setServos(panLoop.m_command, tiltLoop.m_command);
  }
  else if (searchMode)
  {
    // Aucun objet détecté, continuer le balayage
    performSearch();
  }
  else
  {
    // Réinitialiser les boucles PID et les servos si objet perdu
    panLoop.reset();
    tiltLoop.reset();
    pixy.setServos(panLoop.m_command, tiltLoop.m_command);
  }
}

void performSearch()
{
  unsigned long currentTime = millis();
  
  if (currentTime - lastMoveTime >= moveInterval)
  {
    // Changer de direction horizontale après chaque intervalle de mouvement
    switch (currentDirection)
    {
      case LEFT:
        panPosition = 0;
        currentDirection = CENTER;
        break;
      case CENTER:
        panPosition = 500;
        currentDirection = RIGHT;
        break;
      case RIGHT:
        panPosition = 1000;
        currentDirection = LEFT;
        break;
    }
    
    // Changer de direction verticale à chaque changement de direction horizontale
    switch (currentVerticalDirection)
    {
      case UP:
        tiltPosition = 200; // Modifier pour regarder vers le haut
        currentVerticalDirection = DOWN;
        break;
      case DOWN:
        tiltPosition = 800; // Modifier pour regarder vers le bas
        currentVerticalDirection = UP;
        break;
    }
    
    // Mettre à jour les positions des servos pour commencer le mouvement
    pixy.setServos(panPosition, tiltPosition);
    
    lastMoveTime = currentTime;
  }
}
