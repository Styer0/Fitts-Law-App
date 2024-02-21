import tkinter as tk

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Fitts Law Game")
        master.geometry('1200x900')
        
        title_label = tk.Label(master, text="Fitts Law Game!", font=("Consolas", 20))
        title_label.pack(pady=200)