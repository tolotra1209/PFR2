import tkinter as tk

class show_bluetooth:
    def __init__(self):
        self.create_buttons()
        self.create_label()
        pass
    def show_bluetooths(self):
        #self..hide_all_buttons()

        self.bannerButton8.place(x=25, y=75)
        self.search_button.place(x=75,y=150)
        self.appareil_label.place(x=100, y=200)
        self.devices_listbox.place(x=50, y=250)
        self.connect_button.place(x=150, y=450)

        pass