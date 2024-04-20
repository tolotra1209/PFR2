import tkinter as tk
from bluetooth import BluetoothController
from speech_recognition import SpeechRecognizer
from video_stream import VideoStream
from colors import couleur
from show_bluetooth import show_bluetooth

blueto=show_bluetooth()

class AppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Control")
        self.master.config(bg="gray30")
        self.master.geometry("400x600")
        self.master.iconbitmap("logo.ico")

        self.bluetooth_controller = BluetoothController()
        self.speech_recognizer = SpeechRecognizer()
        self.video_stream = VideoStream()

        self.blueto=show_bluetooth()

        # Other GUI initialization and layout code goes here
    def create_buttons(self):
        # Créez tous les boutons ici, mais ne les placez pas sur la fenêtre encore
        self.bannerButton = tk.Button(self.master, text="STOP", font="ExtraCondensed 32",
                                      fg="black", bd=0, bg=couleur["Rouge"], command=None)

        self.bannerButton1 = tk.Button(self.master, text="AUTO", font="ExtraCondensed 32",
                                       width=7, height=1, fg="black", bd=0, bg=couleur["Cyan"],
                                       command=self.show_auto)

        self.bannerButton2 = tk.Button(self.master, text="MANU", font="ExtraCondensed 32",
                                       width=7, height=1, fg="black", bd=0, bg=couleur["Cyan"],
                                       command=self.show_manu)

        self.bannerButton3 = tk.Button(self.master, text="VOCAL", font="ExtraCondensed 32",
                                       width=7, height=1, fg="black", bd=0, bg=couleur["Cyan"],
                                       command=self.show_vocal)

        self.bannerButton4 = tk.Button(self.master, text="RETOUR", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=couleur["Gris"], command=self.show_modes)

        self.bannerButton5 = tk.Button(self.master, text="LANGUES", font="ExtraCondensed 32",
                                       width=12, height=1, fg="black", bd=0, bg=couleur["Cyan"],
                                       command=self.show_langue)

        self.bannerButton6 = tk.Button(self.master, text="ANGLAIS", font="ExtraCondensed 32",
                                       fg="black", bd=0, bg=couleur["Cyan"], command=self.anglais)

        self.bannerButton7 = tk.Button(self.master, text="FRANCAIS", font="ExtraCondensed 32",
                                       fg="black", bd=0, bg=couleur["Cyan"], command=None)

        self.bannerButton8 = tk.Button(self.master, text="RETOUR", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=couleur["Gris"], command=self.show_parametres)

        self.bannerButton9 = tk.Button(self.master, text="PARLEZ", font="ExtraCondensed 20",
                                       fg="black", bd=0, bg=couleur["Vert"], command=self.choose_voice)

        self.bannerButton10 = tk.Button(self.master, text="BLUETOOTH", font="ExtraCondensed 32",
                                        width=12, height=1, fg="black", bd=0, bg=couleur["Cyan"],
                                        command=self.show_bluetooth)

        self.search_button = tk.Button(self.master, text="Rechercher des appareils", font="ExtraCondensed 15",
                                       fg="black", bd=0, bg=couleur["Jaune"], command=self.search_devices)

        self.connect_button = tk.Button(self.master, text="Se connecter", font="ExtraCondensed 15",
                                        fg="black", bd=0, bg=couleur["Vert"], command=self.connect_to_selected_device)
        # Créez tous les autres boutons de la même manière...

    def show_auto(self):
        # Affichez seulement les boutons pour le mode AUTO
        self.hide_all_buttons()  # Cachez tous les boutons d'abord
        self.bannerButton1.place(x=110, y=150)  # Placez le bouton AUTO sur la fenêtre
        # Placez les autres boutons nécessaires pour le mode AUTO, si nécessaire

    def show_manu(self):
        # Affichez seulement les boutons pour le mode MANU
        self.hide_all_buttons()
        self.bannerButton2.place(x=110, y=150)

    # Définissez des méthodes similaires pour les autres modes et fenêtres

    def hide_all_buttons(self):
        # Cachez tous les boutons
        self.bannerButton.place_forget()
        self.bannerButton1.place_forget()
        self.bannerButton2.place_forget()
        self.bannerButton3.place_forget()
        self.bannerButton4.place_forget()
        self.bannerButton5.place_forget()
        self.bannerButton6.place_forget()
        self.bannerButton7.place_forget()
        self.bannerButton8.place_forget()
        self.bannerButton9.place_forget()
        self.bannerButton10.place_forget()
        self.search_button.place_forget()
        self.connect_button.place_forget()
        
    
    
