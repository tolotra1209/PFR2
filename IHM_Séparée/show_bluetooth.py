from boutons import MesBoutons

class show_bluetooth :
    def show_bluetooth():
        bannerButton8.place(x=25, y=75)
        search_button.place(x=75,y=150)
        appareil_label.place(x=100, y=200)
        devices_listbox.place(x=50, y=250)
        connect_button.place(x=150, y=450)
        

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
        if bannerButton5.winfo_exists():
            bannerButton5.place_forget()
        if bannerButton6.winfo_exists():
            bannerButton6.place_forget()
        if bannerButton7.winfo_exists():
            bannerButton7.place_forget()
        if bannerButton9.winfo_exists():
            bannerButton9.place_forget()
        if bannerButton10.winfo_exists():
            bannerButton10.place_forget()
        

        #suppression de texte
        if auto_label.winfo_exists():
            auto_label.place_forget()
        if manu_label.winfo_exists():
            manu_label.place_forget()
        if result_label.winfo_exists():
            result_label.place_forget()
        if vocal_label.winfo_exists():
            vocal_label.place_forget()