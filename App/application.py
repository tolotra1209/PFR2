import tkinter as tk
from tkinter import PhotoImage

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
        bannerTexte.config(fg=couleur["Noir"])
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
    bannerTexte.config(text="LET'S \nCONTROL \nROBOT")

def show_mapping():
    accueilText.config(text="MAPPING")
    bannerTexte.config(text="MAPPING \nBORDER")

def show_mode():
    accueilText.config(text="MODE")
    bannerTexte.config(text="CHOOSE \n YOUR MODE")

def show_tracking():
    accueilText.config(text="TRACKING")
    bannerTexte.config(text="TRACKING A \nRED BALL")

def show_parametres():
    accueilText.config(text="PARAMETRES")
    bannerTexte.config(text="MAKE YOUR \nSETTING")


# Barre de navigation Top
topFrame = tk.Frame(app, bg=couleur["Bleu"])
topFrame.pack(side="top", fill=tk.X)


# Texte de top
accueilText = tk.Label(topFrame, text="ACCUEIL", font="ExtraCondensed 15",
                       bg=couleur["Bleu"], fg="white", height=2, padx=20)
accueilText.pack(side="right")

# Banner text & Image de fond
can = tk.Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=tk.NW, image=imgFond)
bannerTexte = tk.Label(app, text="LET'S \nCONTROL \nROBOT", font="ExtraCondensed 32",
                       fg="black")
bannerTexte.place(x=60, y=400)
can.pack()

# Icone
robIcon = tk.Button(topFrame, image=ouvIcon, bg=couleur["Bleu"],
                    bd=0, padx=20, activebackground=couleur["Bleu"], command=switch)
robIcon.place(x=10, y=10)

#bouton ecran


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

app.resizable(width=False, height=False)

app.mainloop()
