import socket
import bluetooth

# Recherche des appareils Bluetooth disponibles
print("Recherche d'appareils Bluetooth disponibles...")
nearby_devices = bluetooth.discover_devices()

# Affichage des appareils trouvés
print("Appareils Bluetooth disponibles :")
for i, device_address in enumerate(nearby_devices):
    print(f"{i + 1}: {bluetooth.lookup_name(device_address)} [{device_address}]")

# Demande à l'utilisateur de sélectionner l'appareil auquel se connecter
selected_device_index = int(input("Sélectionnez le numéro de l'appareil auquel vous souhaitez vous connecter : ")) - 1
selected_device_address = nearby_devices[selected_device_index]

# Port pour le service RFCOMM
port = 3

# Création d'une socket Bluetooth
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    # Connexion au serveur Bluetooth
    s.connect((selected_device_address, port))
    print("Connecté avec succès au serveur Bluetooth.")
    
    # Envoi des messages au serveur
    while True:
        text = input("Entrez votre message (ou 'quit' pour quitter) : ")
        s.send(bytes(text, 'UTF-8'))
        if text.lower() == "quit":
            break

except bluetooth.btcommon.BluetoothError as e:
    print("Erreur de connexion Bluetooth :", e)

except ConnectionResetError:
    print("La connexion avec le serveur a été réinitialisée.")

except ConnectionAbortedError:
    print("La connexion avec le serveur a été interrompue.")

finally:
    # Fermeture de la socket
    s.close()
    print("Connexion au serveur Bluetooth fermée.")
