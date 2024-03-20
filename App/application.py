import tkinter as tk
from tkinter import PhotoImage
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
        result_label.config(text="Vous avez dit: \n" + text)
    except sr.UnknownValueError:
        result_label.config(text="Google Speech Recognition n'a pas pu comprendre l'audio.")
    except sr.RequestError as e:
        result_label.config(text="Impossible d'accéder à l'API Google Speech Recognition : " + str(e))

def choose_voice():
    #label.config(text="Commande vocale sélectionnée")
    result_label.config(text="Parlez maintenant...")  # Afficher "Parlez maintenant"
    app.update()  # Mettre à jour l'interface graphique

    recognize_speech()

    # Réinitialiser le texte du label résultat après que "Vous avez dit" apparaisse
    result_label.after(5000, lambda: result_label.config(text=""))

# Dictionnaire de couleur
couleur = {
    "Blanc": "#FFFFFF", "Noir": "#000000", "Rouge": "#FF0000",
    "Vert": "#00FF00", "Bleu": "#0000FF", "Jaune": "#FFFF00",
    "Cyan": "#00FFFF", "Magenta": "#FF00FF", "Gris": "#808080",
    "Vert clair": "#90EE90", "Bleu ciel": "#87CEEB"
}

# Paramétrage de la fenêtre
app = tk.Tk()
app.title("Robot Control")
app.config(bg="gray30")
app.geometry("400x600")
app.iconbitmap("logo.ico")  # You need to have 'logo.ico' file in the directory

# Paramètrage switch
boutonEtat = False

# Chargement image
ouvIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file='close.png')
imgFond = PhotoImage(file='rover.png')


# Définir les fonctions switch
def switch():
    global boutonEtat
    if boutonEtat is True:
        # Créer une fermeture animé
        for x in range(300):
            framLateral.place(x=-x, y=0)
            topFrame.update()

        # reset couleur widgets
        bannerButton.config(fg=couleur["Noir"])
        accueilText.config(bg=couleur["Bleu"])
        topFrame.config(bg=couleur["Bleu"])
        app.config(bg="gray30")
        boutonEtat = False
    else:
        for x in range(-300, 0):
            framLateral.place(x=x, y=0)
            topFrame.update()
            boutonEtat = True

# Définir les fonctions pour les options
def show_accueil():
    accueilText.config(text="ACCUEIL")
    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()

    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()

def show_mapping():
    accueilText.config(text="MAPPING")
    #ajout de bouton
    bannerButton.place(x=100,y=150)

    #suppression de bouton
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()
    
    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()
        

def show_mode():
    accueilText.config(text="MODE")
    #ajout de bouton
    bannerButton1.place(x=100,y=150)
    bannerButton2.place(x=100,y=250)
    bannerButton3.place(x=100,y=350)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()

    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()
    


def show_tracking():
    accueilText.config(text="TRACKING")
    #ajout de bouton

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()
    
    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()

def show_parametres():
    accueilText.config(text="PARAMETRES")
    #ajout de bouton
    bannerButton5.place(x=100, y=200)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()

    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()

#Définir les fonctions pour MODE
def show_auto():
    bannerButton4.place(x=25, y=75)
    #ajout de texte
    auto_label.place(x=100, y=350)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()
    
    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()
    

def show_manu():
    bannerButton4.place(x=25, y=75)
    #ajout de texte
    manu_label.place(x=100, y=350)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()

    #suppression de texte
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()

def show_vocal():
    bannerButton4.place(x=25, y=75)
    bannerButton9.place(x=125, y=350)

    #ajout de texte
    vocal_label.place(x=50, y=150)
    result_label.place(x=50, y=250)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    
    

    #suppression de texte
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    
    
    

#Définir les fonctions pour PARAMETRE
def show_langue():
    bannerButton6.place(x=100, y=200)
    bannerButton7.place(x=100, y=300)
    bannerButton8.place(x=25, y=75)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton5.winfo_exists():
        bannerButton5.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()
    

    #suppression de texte
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()
    if vocal_label.winfo_exists():
        vocal_label.place_forget()

# Barre de navigation Top
topFrame = tk.Frame(app, bg=couleur["Bleu"])
topFrame.pack(side="top", fill=tk.X)


# Texte de top
accueilText = tk.Label(topFrame, text="ACCUEIL", font="ExtraCondensed 15",
                       bg=couleur["Bleu"], fg="white", height=2, padx=20)
accueilText.pack(side="right")

# Banner Button & Image de fond
can = tk.Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=tk.NW, image=imgFond)


bannerButton = tk.Button(app, text="STOP", font="ExtraCondensed 32",
                         fg="black", bd=0, bg=couleur["Rouge"], command=None)

bannerButton1 = tk.Button(app, text="AUTO", font="ExtraCondensed 32",
                          fg="black", bd=0, bg=couleur["Jaune"], command=show_auto)

bannerButton2 = tk.Button(app, text="MANU", font="ExtraCondensed 32",
                            fg="black", bd=0, bg=couleur["Vert"], command=show_manu)

bannerButton3 = tk.Button(app, text="VOCAL", font="ExtraCondensed 32",
                            fg="black", bd=0, bg=couleur["Cyan"], command=show_vocal)

bannerButton4 = tk.Button(app, text="RETOUR", font="ExtraCondensed 20",
                            fg="black", bd=0, bg=couleur["Gris"], command=show_mode)

bannerButton5 = tk.Button(app, text="LANGUES", font="ExtraCondensed 32",
                            fg="black", bd=0, bg=couleur["Cyan"], command=show_langue)

bannerButton6 = tk.Button(app, text="ANGLAIS", font="ExtraCondensed 32",
                            fg="black", bd=0, bg=couleur["Vert"], command=None)

bannerButton7 = tk.Button(app, text="FRANCAIS", font="ExtraCondensed 32",
                            fg="black", bd=0, bg=couleur["Vert"], command=None)

bannerButton8 = tk.Button(app, text="RETOUR", font="ExtraCondensed 20",
                            fg="black", bd=0, bg=couleur["Gris"], command=show_parametres)

bannerButton9 = tk.Button(app, text="PARLEZ", font="ExtraCondensed 20",
                            fg="black", bd=0, bg=couleur["Vert"], command=choose_voice)

can.pack()

#Bouton 

#Label d'affichage
auto_label = tk.Label(app, text="Veuillez patientez...")

manu_label = tk.Label(app, text="Utiliser les boutons de direction \npour controler le robot")

vocal_label = tk.Label(app, text="Commande vocal séléctionnée...", font="ExtraCondensed 15")

# Icone
robIcon = tk.Button(topFrame, image=ouvIcon, bg=couleur["Bleu"],
                    bd=0, padx=20, activebackground=couleur["Bleu"], command=switch)
robIcon.place(x=10, y=10)

# Parametre laterale
framLateral = tk.Frame(app, bg="gray30", width=300, height=600)
framLateral.place(x=-300, y=0)
tk.Label(framLateral, font="ExtraCondensed 15", bg=couleur["Bleu"],
         fg="black", width=300, height=2, padx=20).place(x=0, y=0)
y = 60

# Les options dans la NavBar Laterale
options = ["ACCUEIL", "MAPPING", "MODE", "TRACKING", "PARAMETRES"]

# Positionnement des options dans la NavBar
for i, option in enumerate(options):
    command = globals()["show_" + option.lower()]
    tk.Button(framLateral, text=option, font="ExtraCondensed 15", bg="gray30",
              fg=couleur["Blanc"], activebackground="gray30", bd=0, command=lambda cmd=command: [cmd(), switch()]).place(x=25, y=y)
    

    y += 40

# Paramétrage bouton fermeture menu
fermeBouton = tk.Button(framLateral, image=closeIcon, bg=couleur["Bleu"],
                        activebackground=couleur["Bleu"],
                        bd=0, command=switch)
fermeBouton.place(x=250, y=10)

# Création et ajout d'un widget Label pour afficher le résultat de la reconnaissance vocale
result_label = tk.Label(app, text="",font="ExtraCondensed 20" )



app.resizable(width=False, height=False)

app.mainloop()
