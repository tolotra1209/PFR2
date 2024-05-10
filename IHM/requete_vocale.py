import tkinter as tk
import serial
import speech_recognition as sr

# Configuration de la communication série avec l'Arduino
arduino_port = 'COM8'
arduino_baudrate = 9600
ser = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

# Chargement des verbes depuis le fichier
with open('verbe.txt', 'r') as file:
    verbe_liste = file.read().splitlines()

# Fonction pour vérifier si un mot est un verbe et l'écrire dans un fichier texte
def verifier_et_ecrire_verbe(mot):
    if mot in verbe_liste:
        with open('verbe_enregistre.txt', 'w') as enregistre_file:
            enregistre_file.write(mot)

# Fonction pour enregistrer la voix et vérifier les verbes
def enregistrer_et_sauvegarder():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Dites quelque chose...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Analyse du discours...")
        texte = recognizer.recognize_google(audio, language='fr-FR') 
        print("Vous avez dit:", texte)
        if texte.lower() == "stoppe" or texte.lower() == "stop":
            print("Fonction vocale arrêtée.")
            return "stoppe"  
        mots = texte.split()  
        verbes = [mot.lower() for mot in mots if mot.lower() in verbe_liste] 
        if verbes:
            with open('verbe_enregistre.txt', 'w') as enregistre_file:
                enregistre_file.write('\n'.join(verbes))  
        # Sauvegarder la phrase complète dans un fichier
        with open('texte_enregistre.txt', 'w') as enregistre_file:
            enregistre_file.write(texte)
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print("Erreur lors de la demande de service : {0}".format(e))
    except KeyboardInterrupt:
        raise SystemExit

# Fonctions pour envoyer des commandes à l'Arduino
def envoyer_commande(commande):
    ser.write(commande.encode())  
    print("Commande envoyée:", commande)

# Fonction principale pour écouter et enregistrer le texte
def ecouter_et_enregistrer():
    while True:
        try:
            verbe = enregistrer_et_sauvegarder()
            if verbe == "stoppe":
                print("Arrêt du programme...")
                break
            elif verbe.lower() == "avancer":
                envoyer_commande("avancer\n")
            elif verbe.lower() == "gauche":
                envoyer_commande("gauche\n")
            elif verbe.lower() == "droite":
                envoyer_commande("droite\n")
            elif verbe.lower() == "arreter":
                envoyer_commande("arreter\n")
            else:
                print("Verbe non reconnu.")
        except KeyboardInterrupt:
            print("Arrêt du programme...")
            break

# Création de l'interface graphique
root = tk.Tk()
root.title("Contrôle du robot")

# Bouton pour enregistrer la voix et contrôler le robot
btn_voix = tk.Button(root, text="Contrôler par la voix", command=ecouter_et_enregistrer)
btn_voix.pack()

# Fonction pour fermer le port série lorsque l'interface graphique est fermée
def fermer_port_serie():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", fermer_port_serie)
root.mainloop()
