from boutons import MesBoutons

class show_modes :
    def show_modes():
        accueilText.config(text="MODES")
        #ajout de bouton
        bannerButton1.place(x=110,y=150)
        bannerButton2.place(x=110,y=250)
        bannerButton3.place(x=110,y=350)

        #suppression de bouton
        if bannerButton.winfo_exists():
            bannerButton.place_forget()
        if bannerButton4.winfo_exists():
            bannerButton4.place_forget()
        if bannerButton5.winfo_exists():
            bannerButton5.place_forget()
        if bannerButton6.winfo_exists():
            bannerButton6.place_forget()
        if bannerButton7.winfo_exists():
            bannerButton7.place_forget()
        if bannerButton8.winfo_exists():
            bannerButton8.place_forget()
        if bannerButton9.winfo_exists():
            bannerButton9.place_forget()
        if bannerButton10.winfo_exists():
            bannerButton10.place_forget()
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