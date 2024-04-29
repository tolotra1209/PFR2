import tkinter as tk
from tkinter import *
from fenetre import app
from show_auto import show_auto
from show_manu import show_manu
from show_vocal import show_vocal
from show_modes import show_modes
from show_langue import show_langue
from show_parametres import show_parametres
from choose_voice import choose_voice
from show_bluetooth import show_bluetooth
from search_devices import search_devices
from connect_to_selected_device import connect_to_selected_device
from .run_english_app import run_english_app

class MesBoutons :
    # Dictionnaire de couleur
    couleur = {
        "Blanc": "#FFFFFF", "Noir": "#000000", "Rouge": "#FF0000",
        "Vert": "#00FF00", "Bleu": "#0000FF", "Jaune": "#FFFF00",
        "Cyan": "#00FFFF", "Magenta": "#FF00FF", "Gris": "#808080",
        "Vert clair": "#90EE90", "Bleu ciel": "#87CEEB"
    }

    imgFond = PhotoImage(file='fond.png')

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

    bannerButton1 = tk.Button(app, text="AUTO", font="ExtraCondensed 32",width=7,height=1,
                            fg="black", bd=0, bg=couleur["Cyan"], command=show_auto)

    bannerButton2 = tk.Button(app, text="MANU", font="ExtraCondensed 32",width=7,height=1,
                                fg="black", bd=0, bg=couleur["Cyan"], command=show_manu)

    bannerButton3 = tk.Button(app, text="VOCAL", font="ExtraCondensed 32",width=7,height=1,
                                fg="black", bd=0, bg=couleur["Cyan"], command=show_vocal)

    bannerButton4 = tk.Button(app, text="RETOUR", font="ExtraCondensed 20",
                                fg="black", bd=0, bg=couleur["Gris"], command=show_modes)

    bannerButton5 = tk.Button(app, text="LANGUES", font="ExtraCondensed 32",width=12,height=1,
                                fg="black", bd=0, bg=couleur["Cyan"], command=show_langue)

    bannerButton6 = tk.Button(app, text="ANGLAIS", font="ExtraCondensed 32",
                                fg="black", bd=0, bg=couleur["Cyan"], command=run_english_app)

    bannerButton7 = tk.Button(app, text="FRANCAIS", font="ExtraCondensed 32",
                                fg="black", bd=0, bg=couleur["Cyan"], command=None)

    bannerButton8 = tk.Button(app, text="RETOUR", font="ExtraCondensed 20",
                                fg="black", bd=0, bg=couleur["Gris"], command=show_parametres)

    bannerButton9 = tk.Button(app, text="PARLEZ", font="ExtraCondensed 20",
                                fg="black", bd=0, bg=couleur["Vert"], command=choose_voice)

    bannerButton10 = tk.Button(app, text="BLUETOOTH", font="ExtraCondensed 32",width=12,height=1,
                                fg="black", bd=0, bg=couleur["Cyan"], command=show_bluetooth)

    search_button = tk.Button(app, text="Rechercher des appareils", font="ExtraCondensed 15",
                            fg="black", bd=0, bg=couleur["Jaune"], command=search_devices)

    connect_button = tk.Button(app, text="Se connecter",font="ExtraCondensed 15",
                            fg="black", bd=0, bg=couleur["Vert"], command=connect_to_selected_device)

    can.pack()