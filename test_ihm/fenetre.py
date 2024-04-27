import tkinter as tk

class MaFenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ma Fenêtre avec Tkinter")
        self.geometry("300x200")  # Définir la taille de la fenêtre
        
        self.label = self.creer_label("Bienvenue !", 0.5, 0.1)
        self.bouton1 = self.creer_bouton("Bouton 1", self.action_bouton1, 0.5, 0.4)
        self.bouton2 = self.creer_bouton("Bouton 2", self.action_bouton2, 0.5, 0.6)
        
    def creer_label(self, texte, relx, rely):
        label = tk.Label(self, text=texte)
        label.place(relx=relx, rely=rely, anchor="center")
        return label
        
    def creer_bouton(self, texte, commande, relx, rely):
        bouton = tk.Button(self, text=texte, command=commande)
        bouton.place(relx=relx, rely=rely, anchor="center")
        return bouton
        
    def action_bouton1(self):
        self.label.config(text="Bouton 1 cliqué !")
        
    def action_bouton2(self):
        self.label.config(text="Bouton 2 cliqué !")
