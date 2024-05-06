import tkinter as tk
from tkinter import ttk
import turtle
from requete_vocale import ecouter_et_enregistrer

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

def translate_to_english():
    button_connecter.config(text="Connect")
    button_deconnecter.config(text="Disconnect")
    button_manuel.config(text="Manual")
    button_auto.config(text="Auto")
    button_voix.config(text="Voice")
    button_stop.config(text="Stop")
    button_update.config(text="Update")

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
root.attributes('-fullscreen', True)

# Création d'une frame pour contenir les éléments
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, anchor=tk.SW, padx=20, pady=20)  # Décalage de 20 pixels à gauche et en haut

button_close = tk.Button(root, text="  X  ", command=close_window, bg="red", fg="white")
button_close.pack(side=tk.TOP, anchor=tk.NE)

# Ajouter une liste déroulante de langue
languages = ["Français", "English"]
language_combobox = ttk.Combobox(frame, values=languages, state="readonly")
language_combobox.current(0)  # Français par défaut
language_combobox.bind("<<ComboboxSelected>>", on_language_change)
language_combobox.grid(row=0, column=1, padx=10, pady=10, sticky='ew')  # Positionnement au-dessus des boutons

# Ajouter des boutons de connexion
button_connecter = tk.Button(frame, text="Connecter", width=10, bg="yellow")
button_connecter.grid(row=1, column=0, padx=10, pady=10, sticky='ew')  # Centre les boutons en leur donnant une largeur élastique

button_deconnecter = tk.Button(frame, text="Déconnecter", width=10)
button_deconnecter.grid(row=1, column=2, padx=10, pady=10, sticky='ew')

# Ajouter des boutons de mode
button_manuel = tk.Button(frame, text="Manuel", width=7)
button_manuel.grid(row=2, column=0, padx=10, pady=10)  # Placer les boutons un peu plus haut

button_auto = tk.Button(frame, text="Auto", width=7)
button_auto.grid(row=2, column=1, padx=10, pady=10)

button_voix = tk.Button(frame, text="Voix", width=7, command=ecouter_et_enregistrer)
button_voix.grid(row=2, column=2, padx=10, pady=10)

# Ajouter des boutons de direction en croix
button_up = tk.Button(frame, text="↑", width=5, height=2, command=draw_turtle_up)
button_up.grid(row=3, column=1, padx=10, pady=10)  # Placer le bouton en haut au centre

button_down = tk.Button(frame, text="↓", width=5, height=2, command=draw_turtle_down)
button_down.grid(row=5, column=1, padx=10, pady=10)  # Placer le bouton en bas au centre

button_left = tk.Button(frame, text="←", width=5, height=2, command=draw_turtle_left)
button_left.grid(row=4, column=0, padx=10, pady=10)  # Placer le bouton à gauche au centre

button_right = tk.Button(frame, text="→", width=5, height=2, command=draw_turtle_right)
button_right.grid(row=4, column=2, padx=10, pady=10)  # Placer le bouton à droite au centre

# Ajouter le bouton "stop" au centre de l'écran
button_stop = tk.Button(frame, text="Stop", width=5, height=2, bg="red", fg="white")
button_stop.grid(row=4, column=1, padx=10, pady=10)

# Cadre de turtle en haut à gauche
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=20)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

# Conteneur pour la carte turtle et le bouton Effacer
turtle_frame = tk.Frame(root)
turtle_frame.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=10)

# Bouton pour effacer le turtle et recentrer
button_update = tk.Button(turtle_frame, text="Actualiser", width=7, command=clear_turtle)
button_update.pack(side=tk.LEFT, padx=150)

root.mainloop()