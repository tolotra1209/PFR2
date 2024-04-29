class connect_to_selected_device :
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