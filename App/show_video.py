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