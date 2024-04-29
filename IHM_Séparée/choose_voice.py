import tkinter as tk
import speech_recognition as sr
from recognize_speech import recognize_speech

class choose_voice :
    def choose_voice():
        result_label = tk.Label(app, text="",font="ExtraCondensed 20" )
        app = tk.Tk()
        #label.config(text="Commande vocale sélectionnée")
        result_label.config(text="Parlez maintenant...")  # Afficher "Parlez maintenant"
        app.update()  # Mettre à jour l'interface graphique

        recognize_speech()

        # Réinitialiser le texte du label résultat après que "Vous avez dit" apparaisse
        result_label.after(5000, lambda: result_label.config(text=""))