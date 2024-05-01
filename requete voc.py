import speech_recognition as sr

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
        recognizer.adjust_for_ambient_noise(source)  # Réglage automatique du bruit de fond
        audio = recognizer.listen(source)

    try:
        print("Analyse du discours...")
        texte = recognizer.recognize_google(audio, language='fr-FR')  # Reconnaissance vocale en français
        print("Vous avez dit:", texte)
        if texte.lower() == "stoppe":
            print("Programme interrompu.")
            raise KeyboardInterrupt
        mots = texte.split()  # Diviser le texte en mots
        verbes = [mot.lower() for mot in mots if mot.lower() in verbe_liste]  # Filtrer les verbes
        if verbes:
            with open('verbe_enregistre.txt', 'w') as enregistre_file:
                enregistre_file.write('\n'.join(verbes))  # Enregistrer tous les verbes trouvés
        # Sauvegarder la phrase complète dans un fichier
        with open('texte_enregistre.txt', 'w') as enregistre_file:
            enregistre_file.write(texte)
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print("Erreur lors de la demande de service : {0}".format(e))
    except KeyboardInterrupt:
        raise SystemExit

# Fonction principale pour écouter et enregistrer le texte
def ecouter_et_enregistrer():
    while True:
        enregistrer_et_sauvegarder()

# Appel de la fonction principale
if __name__ == "__main__":
    ecouter_et_enregistrer()
