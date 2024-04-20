import bluetooth
import socket
import tkinter as tk
from tkinter import messagebox

class BluetoothController:
    def __init__(self):
        self.nearby_devices = []

    def search_devices(self):
        self.nearby_devices = bluetooth.discover_devices()
        self.update_devices_list()

    def connect_to_selected_device(self, devices_listbox):
        selected_index = devices_listbox.curselection()
        if selected_index:
            selected_device_index = int(selected_index[0])
            selected_device_address = self.nearby_devices[selected_device_index]
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

    def update_devices_list(self, devices_listbox):
        devices_listbox.delete(0, tk.END)
        for i, device_address in enumerate(self.nearby_devices):
            devices_listbox.insert(tk.END, f"{i + 1}: {bluetooth.lookup_name(device_address)} [{device_address}]")
