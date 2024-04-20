

def show_parametres():
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

    accueilText.config(text="PARAMETRES")
    #ajout de bouton
    bannerButton5.place(x=50, y=200)
    bannerButton10.place(x=50, y=300)

    #suppression de bouton
    if bannerButton.winfo_exists():
        bannerButton.place_forget()
    if bannerButton1.winfo_exists():
        bannerButton1.place_forget()
    if bannerButton2.winfo_exists():
        bannerButton2.place_forget()
    if bannerButton3.winfo_exists():
        bannerButton3.place_forget()
    if bannerButton4.winfo_exists():
        bannerButton4.place_forget()
    if bannerButton6.winfo_exists():
        bannerButton6.place_forget()
    if bannerButton7.winfo_exists():
        bannerButton7.place_forget()
    if bannerButton8.winfo_exists():
        bannerButton8.place_forget()
    if bannerButton9.winfo_exists():
        bannerButton9.place_forget()
    if devices_listbox.winfo_exists():
        devices_listbox.place_forget()
    if search_button.winfo_exists():
        search_button.place_forget()
    if connect_button.winfo_exists():
        connect_button.place_forget()

    #suppression de texte
    if vocal_label.winfo_exists():
        vocal_label.place_forget()
    if manu_label.winfo_exists():
        manu_label.place_forget()
    if auto_label.winfo_exists():
        auto_label.place_forget()
    if result_label.winfo_exists():
        result_label.place_forget()
    if appareil_label.winfo_exists():
        appareil_label.place_forget()
    
    pass