import tkinter as tk
from tkinter import PhotoImage, messagebox
import bluetooth
import socket
import cv2
import speech_recognition as sr
from PIL import Image, ImageTk


class VideoStream:
    def __init__(self, app):
        self.app = app
        self.panel = tk.Label(self.app)
        self.cap = cv2.VideoCapture(0)

    def show_video_stream(self):
        _, frame = self.cap.read()
        if _:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.panel.img = img
            self.panel.config(image=img)
            self.panel.after(10, self.show_video_stream)
        else:
            print("Erreur lors de la capture de l'image.")

    def start_stream(self):
        self.show_video_stream()


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


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        with sr.Microphone() as source:
            print("Parlez maintenant...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio_data = self.recognizer.listen(source)
        return audio_data

    def recognize_speech(self):
        audio_data = self.record_audio()
        try:
            text = self.recognizer.recognize_google(audio_data, language="fr-FR")
            result_label.config(text="Vous avez dit: \n" + text)
        except sr.UnknownValueError:
            result_label.config(text="Google Speech Recognition n'a pas pu comprendre l'audio.")
        except sr.RequestError as e:
            result_label.config(text="Impossible d'accéder à l'API Google Speech Recognition : " + str(e))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot Control")
        self.config(bg="gray30")
        self.geometry("400x600")
        self.iconbitmap("logo.ico")
        self.vs = VideoStream(self)
        self.bt_controller = BluetoothController()
        self.speech_recognition = SpeechRecognition()
        self.result_label = tk.Label(self, text="", font="ExtraCondensed 20")

    def start_video_stream(self):
        self.vs.start_stream()


if __name__ == "__main__":
    app = App()
    app.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot Control")
        self.config(bg="gray30")
        self.geometry("400x600")
        self.iconbitmap("logo.ico")
        self.vs = VideoStream(self)
        self.bt_controller = BluetoothController()
        self.speech_recognition = SpeechRecognition()
        self.result_label = tk.Label(self, text="", font="ExtraCondensed 20")

    def start_video_stream(self):
        self.vs.start_stream()


if __name__ == "__main__":
    app = App()
    app.mainloop()
