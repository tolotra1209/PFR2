from application import accueilText
from application import bannerButton
from application import bannerButton1
from application import bannerButton2
from application import bannerButton3
from application import bannerButton4
from application import bannerButton5
from application import bannerButton6
from application import bannerButton7
from application import bannerButton8
from application import bannerButton9
from application import bannerButton10
from application import bannerButton11
from application import search_button
from application import devices_listbox
from application import connect_button
from application import vocal_label
from application import auto_label
from application import manu_label
from application import result_label
from application import appareil_label

def show_video_stream():
    cap = cv2.VideoCapture(0)  # Utilisez l'index 0 pour la première webcam disponible
    _, frame = cap.read()
    if _:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        panel.img = img  # Gardez une référence pour éviter la suppression par le garbage collector
        panel.config(image=img)
        panel.after(10, show_video_stream)  # Mettre à jour l'image toutes les 10 ms
    else:
        print("Erreur lors de la capture de l'image.")