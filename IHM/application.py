import tkinter as tk
from tkinter import ttk
import turtle
from requete_vocale import ecouter_et_enregistrer
import socket
import bluetooth
from tkinter import messagebox

#Bluetooth

def search_devices():
    global nearby_devices
    nearby_devices = bluetooth.discover_devices()
    update_devices_list()

def connect_to_selected_device():
    selected_index = devices_listbox.curselection()
    if selected_index:
        selected_device_index = int(selected_index[0])
        selected_device_address = nearby_devices[selected_device_index]
        try:
            port = 3
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.connect((selected_device_address, port))
            print("Connecté avec succès au serveur Bluetooth.")
            while True:
                text = input("Entrez votre message (ou 'quit' pour quitter) : ")
                s.send(bytes(text, 'UTF-8'))
                if text.lower() == "quit":
                    break
        except bluetooth.btcommon.BluetoothError as e:
            print("Erreur de connexion Bluetooth :", e)
            messagebox.showerror("Erreur", "Impossible de se connecter à l'appareil sélectionné.")
        finally:
            s.close()
            print("Connexion au serveur Bluetooth fermée.")
    else:
        messagebox.showerror("Erreur", "Aucun appareil sélectionné.")

def update_devices_list():
    devices_listbox.delete(0, tk.END)
    for i, device_address in enumerate(nearby_devices):
        devices_listbox.insert(tk.END, f"{i + 1}: {bluetooth.lookup_name(device_address)} [{device_address}]")

# Fin Bluetooth

def close_window():
    root.destroy()

def on_language_change(event):
    selected_language = language_combobox.get()
    if selected_language == "Français":
        translate_to_french()
    elif selected_language == "English":
        translate_to_english()

def translate_to_french():
    button_connecter.config(text="Connecter")
    button_deconnecter.config(text="Déconnecter")
    button_manuel.config(text="Manuel")
    button_auto.config(text="Auto")
    button_voix.config(text="Voix")
    button_stop.config(text="Stop")
    button_update.config(text="Actualiser")
    button_recherche.config(text="Recherche")

def translate_to_english():
    button_connecter.config(text="Connect")
    button_deconnecter.config(text="Disconnect")
    button_manuel.config(text="Manual")
    button_auto.config(text="Auto")
    button_voix.config(text="Voice")
    button_stop.config(text="Stop")
    button_update.config(text="Update")
    button_recherche.config(text="Research")

def draw_turtle_up():
    t.setheading(90)
    t.forward(10)

def draw_turtle_down():
    t.setheading(270)
    t.forward(10)

def draw_turtle_left():
    t.setheading(180)
    t.forward(10)

def draw_turtle_right():
    t.setheading(0)
    t.forward(10)

def clear_turtle():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

root = tk.Tk()
root.geometry("1000x500")
root.title("ROVER")
root.iconbitmap("logo.ico")
root.resizable(width=False, height=False)

# Ajouter une liste déroulante de langue
languages = ["Français", "English"]
language_combobox = ttk.Combobox(root, values=languages, state="readonly")
language_combobox.current(0)  # Français par défaut
language_combobox.bind("<<ComboboxSelected>>", on_language_change)
language_combobox.place(x = 95, y = 50)  # Positionnement au-dessus des boutons

# Ajouter des boutons de connexion
button_recherche = tk.Button(root, text="Recherche", width=10, command=search_devices)
button_recherche.place(x = 25, y = 100)  # Centre les boutons en leur donnant une largeur élastique

button_connecter = tk.Button(root, text="Connecter", width=10, bg="yellow", command=connect_to_selected_device)
button_connecter.place(x = 125, y = 100)  # Centre les boutons en leur donnant une largeur élastique

button_deconnecter = tk.Button(root, text="Déconnecter", width=10)
button_deconnecter.place(x = 225, y = 100)

# Ajouter des boutons de mode
button_manuel = tk.Button(root, text="Manuel", width=7, height=2)
button_manuel.place(x = 220, y = 320)

button_auto = tk.Button(root, text="Auto", width=7, height=2)
button_auto.place(x = 220, y = 375)

button_voix = tk.Button(root, text="Vocal", width=7, height=2, command=ecouter_et_enregistrer)
button_voix.place(x = 220, y = 430)

# Ajouter des boutons de direction en croix
button_up = tk.Button(root, text="↑", width=5, height=2, command=draw_turtle_up)
button_up.place(x = 100, y = 320)  # Placer le bouton en haut

button_down = tk.Button(root, text="↓", width=5, height=2, command=draw_turtle_down)
button_down.place(x = 100, y = 430)  # Placer le bouton en bas

button_left = tk.Button(root, text="←", width=5, height=2, command=draw_turtle_left)
button_left.place(x = 45, y = 375)  # Placer le bouton à gauche

button_right = tk.Button(root, text="→", width=5, height=2, command=draw_turtle_right)
button_right.place(x = 155, y = 375)  # Placer le bouton à droite

# Ajouter le bouton "stop" au centre de l'écran
button_stop = tk.Button(root, text="Stop", width=5, height=2, bg="red", fg="white")
button_stop.place(x = 100, y = 375)

# Cadre de turtle en haut à gauche
canvas = tk.Canvas(root, width=400, height=400)
canvas.place(x = 575, y = 20)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

# Conteneur pour la carte turtle et le bouton Effacer
turtle_frame = tk.Frame(root)
turtle_frame.place(x = 575, y = 20)

# Bouton pour effacer le turtle et recentrer
button_update = tk.Button(root, text="Actualiser", width=7, command=clear_turtle)
button_update.place(x = 750, y = 450)

#Liste
devices_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=46)
devices_listbox.place(x = 25, y = 140)
nearby_devices = []

root.mainloop()