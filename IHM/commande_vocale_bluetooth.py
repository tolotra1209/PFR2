import serial
import speech_recognition as sr

# Chargement des verbes depuis le fichier
with open('verbe.txt', 'r') as file:
    verbe_liste = file.read().splitlines()

# Configurer la connexion Bluetooth
bluetooth_port = '/dev/rfcomm0'  # mets le bon port
baud_rate = 9600  
bluetooth_conn = serial.Serial(bluetooth_port, baud_rate, timeout=1)

# Fonction pour vérifier si un mot est un verbe et l'écrire dans un fichier texte et envoyer au Bluetooth
def verifier_et_ecrire_verbe(mot):
    if mot in verbe_liste:
        with open('verbe_enregistre.txt', 'w') as enregistre_file:
            enregistre_file.write(mot)
        bluetooth_conn.write(mot.encode())

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
                verbe_str = '\n'.join(verbes)
                enregistre_file.write(verbe_str)
                bluetooth_conn.write(verbe_str.encode())
        with open('texte_enregistre.txt', 'w') as enregistre_file:
            enregistre_file.write(texte)
            bluetooth_conn.write(texte.encode())
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print("Erreur lors de la demande de service : {0}".format(e))

# Appel de la fonction principale
if __name__ == "__main__":
    ecouter_et_enregistrer()
