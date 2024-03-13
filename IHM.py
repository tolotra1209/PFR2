import tkinter as tk
import speech_recognition as sr

# Initialisez le Recognizer
recognizer = sr.Recognizer()

# Fonction pour enregistrer l'audio à partir du microphone
def record_audio():
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source)  # Réglez le bruit ambiant
        audio_data = recognizer.listen(source)  # Enregistrez l'audio à partir du microphone
    return audio_data

# Fonction pour reconnaître la parole à partir de l'audio
def recognize_speech():
    audio_data = record_audio()
    try:
        # Utilisez l'API Google Speech Recognition pour reconnaître la parole
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        result_label.config(text="Vous avez dit: " + text)
    except sr.UnknownValueError:
        result_label.config(text="Google Speech Recognition n'a pas pu comprendre l'audio.")
    except sr.RequestError as e:
        result_label.config(text="Impossible d'accéder à l'API Google Speech Recognition : " + str(e))

# Fonction pour changer la langue en français et afficher les boutons correspondants
def set_language_fr():
    label.config(text="Choisissez un mode:")
    result_label.config(text="")  # Réinitialiser le texte du label résultat
    button_fr.pack_forget()  # Pour faire disparaître le bouton "Français"
    button_manual.pack()
    button_auto.pack()
    button_voice.pack()

# Fonction pour afficher les options de mode manuel
def choose_manual():
    label.config(text="Mode manuel sélectionné")
    result_label.config(text="")  # Réinitialiser le texte du label résultat

# Fonction pour afficher les options de mode automatique
def choose_auto():
    label.config(text="Mode automatique sélectionné")
    result_label.config(text="")  # Réinitialiser le texte du label résultat

# Fonction pour afficher les options de commande vocale
def choose_voice():
    label.config(text="Commande vocale sélectionnée")
    result_label.config(text="Parlez maintenant...")  # Afficher "Parlez maintenant"
    root.update()  # Mettre à jour l'interface graphique

    recognize_speech()

    # Réinitialiser le texte du label résultat après que "Vous avez dit" apparaisse
    result_label.after(5000, lambda: result_label.config(text=""))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Sélection de mode")

# Création et ajout d'un widget Label
label = tk.Label(root, text="Choisissez votre langue:")
label.pack()

# Création et ajout d'un widget Button pour la langue française
button_fr = tk.Button(root, text="Français", command=set_language_fr)
button_fr.pack()

# Création des widgets Button pour les différents modes
button_manual = tk.Button(root, text="Mode manuel", command=choose_manual)
button_auto = tk.Button(root, text="Mode automatique", command=choose_auto)
button_voice = tk.Button(root, text="Commande vocale", command=choose_voice)

# Création et ajout d'un widget Label pour afficher le résultat de la reconnaissance vocale
result_label = tk.Label(root, text="")
result_label.pack()

# Exécution de la boucle principale
root.mainloop()
