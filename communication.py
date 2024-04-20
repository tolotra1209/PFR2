import tkinter as tk
import serial

# Configuration de la communication série avec l'Arduino
arduino_port = '/dev/ttyUSB0'  # Changez ceci en fonction de votre système
arduino_baudrate = 9600
ser = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

# Fonctions pour envoyer des commandes à l'Arduino
def avancer():
    ser.write(b'f')

def reculer():
    ser.write(b'b')

def tourner_gauche():
    ser.write(b'l')

def tourner_droite():
    ser.write(b'r')

def arreter():
    ser.write(b's')

# Création de l'interface graphique
root = tk.Tk()
root.title("Contrôle du robot")

# Boutons pour contrôler le robot
btn_avancer = tk.Button(root, text="Avancer", command=avancer)
btn_avancer.pack()

btn_reculer = tk.Button(root, text="Reculer", command=reculer)
btn_reculer.pack()

btn_gauche = tk.Button(root, text="Tourner à gauche", command=tourner_gauche)
btn_gauche.pack()

btn_droite = tk.Button(root, text="Tourner à droite", command=tourner_droite)
btn_droite.pack()

btn_arreter = tk.Button(root, text="Arrêter", command=arreter)
btn_arreter.pack()

# Fonction pour fermer le port série lorsque l'interface graphique est fermée
def fermer_port_serie():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", fermer_port_serie)
root.mainloop()

#remplacer '/dev/ttyUSB0' par le port série du système (par exemple, 'COM3').
