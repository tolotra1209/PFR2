import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from boutons import MesBoutons

class MaFenetre:
    def __init__(self, master):
        self.master = master
        self.couleur = {
            "Blanc": "#FFFFFF", "Noir": "#000000", "Rouge": "#FF0000",
            "Vert": "#00FF00", "Bleu": "#0000FF", "Jaune": "#FFFF00",
            "Cyan": "#00FFFF", "Magenta": "#FF00FF", "Gris": "#808080",
            "Vert clair": "#90EE90", "Bleu ciel": "#87CEEB"
        }

        self.boutonEtat = False

        self.ouvIcon = PhotoImage(file='menu.png')
        self.closeIcon = PhotoImage(file='close.png')
        self.imgFond = PhotoImage(file='fond.png')

        self.app = tk.Tk()
        self.app.title("Robot Control")
        self.app.config(bg="gray30")
        self.app.geometry("400x600")
        self.app.iconbitmap("logo.ico")

        self.topFrame = tk.Frame(self.app, bg=self.couleur["Bleu"])
        self.topFrame.pack(side="top", fill=tk.X)

        self.accueilText = tk.Label(self.topFrame, text="ACCUEIL", font="ExtraCondensed 15",
                                     bg=self.couleur["Bleu"], fg="white", height=2, padx=20)
        self.accueilText.pack(side="right")

        self.bannerButton = tk.Button(self.app, text="STOP", font="ExtraCondensed 32",
                                       fg="black", bd=0, bg=self.couleur["Rouge"], command=None)

        self.bannerButton1 = tk.Button(self.app, text="AUTO", font="ExtraCondensed 32",width=7,height=1,
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=self.show_auto)

        self.bannerButton2 = tk.Button(self.app, text="MANU", font="ExtraCondensed 32",width=7,height=1,
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=self.show_manu)

        self.bannerButton3 = tk.Button(self.app, text="VOCAL", font="ExtraCondensed 32",width=7,height=1,
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=self.show_vocal)

        self.bannerButton4 = tk.Button(self.app, text="RETOUR", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=self.couleur["Gris"], command=self.show_modes)

        self.bannerButton5 = tk.Button(self.app, text="LANGUES", font="ExtraCondensed 32",width=12,height=1,
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=self.show_langue)

        self.bannerButton6 = tk.Button(self.app, text="ANGLAIS", font="ExtraCondensed 32",
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=self.anglais)

        self.bannerButton7 = tk.Button(self.app, text="FRANCAIS", font="ExtraCondensed 32",
                                       fg="black", bd=0, bg=self.couleur["Cyan"], command=None)

        self.bannerButton8 = tk.Button(self.app, text="RETOUR", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=self.couleur["Gris"], command=self.show_parametres)

        self.bannerButton9 = tk.Button(self.app, text="PARLEZ", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=self.couleur["Vert"], command=self.choose_voice)

        self.bannerButton10 = tk.Button(self.app, text="BLUETOOTH", font="ExtraCondensed 32",width=12,height=1,
                                        fg="black", bd=0, bg=self.couleur["Cyan"], command=self.show_bluetooth)

        self.search_button = tk.Button(self.app, text="Rechercher des appareils", font="ExtraCondensed 15",
                                       fg="black", bd=0, bg=self.couleur["Jaune"], command=self.search_devices)

        self.connect_button = tk.Button(self.app, text="Se connecter",font="ExtraCondensed 15",
                                        fg="black", bd=0, bg=self.couleur["Vert"], command=self.connect_to_selected_device)

        self.can = tk.Canvas(self.app, width=400, height=600)
        self.can.create_image(0, 0, anchor=tk.NW, image=self.imgFond)
        self.can.pack()

        self.robIcon = tk.Button(self.topFrame, image=self.ouvIcon, bg=self.couleur["Bleu"],
                                 bd=0, padx=20, activebackground=self.couleur["Bleu"], command=self.switch)
        self.robIcon.place(x=10, y=10)

        self.framLateral = tk.Frame(self.app, bg="gray30", width=300, height=600)
        self.framLateral.place(x=-300, y=0)
        tk.Label(self.framLateral, font="ExtraCondensed 15", bg=self.couleur["Bleu"],
                 fg="black", width=300, height=2, padx=20).place(x=0, y=0)
        y = 60

        options = ["ACCUEIL", "MAPPING", "MODES", "TRACKING", "PARAMETRES"]
        for i, option in enumerate(options):
            command = getattr(self, "show_" + option.lower())
            tk.Button(self.framLateral, text=option, font="ExtraCondensed 15", bg="gray30",
                      fg=self.couleur["Blanc"], activebackground="gray30", bd=0,
                      command=lambda cmd=command: [cmd(), self.switch()]).place(x=25, y=y)
            y += 40

        self.fermeBouton = tk.Button(self.framLateral, image=self.closeIcon, bg=self.couleur["Bleu"],
                                      activebackground=self.couleur["Bleu"], bd=0, command=self.switch)
        self.fermeBouton.place(x=250, y=10)

        self.auto_label = tk.Label(self.app, text="Veuillez patientez...")

        self.manu_label = tk.Label(self.app, text="Utiliser les boutons de direction \npour controler le robot")

        self.vocal_label = tk.Label(self.app, text="Commande vocal séléctionnée...", font="ExtraCondensed 15")

        self.appareil_label= tk.Label(self.app, text="Appareils disponible", font="ExtraCondensed 15")

        self.connect_label= tk.Label(self.app, text="Se connecter a", font="ExtraCondensed 15")

        self.switch()

    def switch(self):
        if self.boutonEtat == False:
            self.framLateral.place(x=0)
            self.boutonEtat = True
        else:
            self.framLateral.place(x=-300)
            self.boutonEtat = False

    def show_auto(self):
        self.auto_label.place(x=100, y=250)

    def show_manu(self):
        self.manu_label.place(x=100, y=250)

    def show_vocal(self):
        self.vocal_label.place(x=100, y=250)

    def show_modes(self):
        self.auto_label.place_forget()
        self.manu_label.place_forget()
        self.vocal_label.place_forget()

    def show_langue(self):
        self.bannerButton5.place_forget()
        self.bannerButton6.place(x=50, y=250)
        self.bannerButton7.place(x=250, y=250)
        self.bannerButton8.place(x=0, y=0)

    def anglais(self):
        self.app.title("Robot Control")
        self.accueilText.config(text="WELCOME")
        self.bannerButton.config(text="STOP")
        self.bannerButton1.config(text="AUTO")
        self.bannerButton2.config(text="MANU")
        self.bannerButton3.config(text="VOICE")
        self.bannerButton4.config(text="BACK")
        self.bannerButton5.config(text="LANGUAGES")
        self.bannerButton6.config(text="ENGLISH", command=None)
        self.bannerButton7.config(text="FRENCH", command=self.francais)
        self.bannerButton8.config(text="BACK")
        self.bannerButton9.config(text="SPEAK")
        self.bannerButton10.config(text="BLUETOOTH")
        self.auto_label.config(text="Please wait...")
        self.manu_label.config(text="Use direction buttons \nto control the robot")
        self.vocal_label.config(text="Voice command selected...")

    def francais(self):
        self.app.title("Control du Robot")
        self.accueilText.config(text="ACCUEIL")
        self.bannerButton.config(text="ARRET")
        self.bannerButton1.config(text="AUTO")
        self.bannerButton2.config(text="MANU")
        self.bannerButton3.config(text="VOCAL")
        self.bannerButton4.config(text="RETOUR")
        self.bannerButton5.config(text="LANGUES")
        self.bannerButton6.config(text="ANGLAIS", command=self.anglais)
        self.bannerButton7.config(text="FRANCAIS", command=None)
        self.bannerButton8.config(text="RETOUR")
        self.bannerButton9.config(text="PARLER")
        self.bannerButton10.config(text="BLUETOOTH")
        self.auto_label.config(text="Veuillez patientez...")
        self.manu_label.config(text="Utiliser les boutons de direction \npour controler le robot")
        self.vocal_label.config(text="Commande vocal séléctionnée...")

    def show_parametres(self):
        self.bannerButton5.place(x=50, y=250)
        self.bannerButton6.place_forget()
        self.bannerButton7.place_forget()
        self.bannerButton8.place_forget()

    def show_bluetooth(self):
        self.appareil_label.place(x=100, y=250)
        self.search_button.place(x=100, y=300)
        self.connect_button.place(x=100, y=350)

    def search_devices(self):
        pass

    def connect_to_selected_device(self):
        pass

    def choose_voice(self):
        pass

    def run(self):
        self.app.mainloop()

# Création de l'instance de la fenêtre et exécution
if __name__ == "__main__":
    app = MaFenetre(tk.Tk())
    app.run()
