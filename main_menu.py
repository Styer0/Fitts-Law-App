import tkinter as tk

myFont = ("Consolas", 20)
class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Fitts Law Game")
        master.geometry('1200x900')
        
        title_label = tk.Label(master, text="Fitts Law Game!", font=myFont)
        title_label.pack(pady=200)
        
        start_btn = ""
        settings_btn = ""
        
        exit_btn = tk.Button(master, text="Exit", command=self.exit_app)
        exit_btn['font'] = myFont
        exit_btn.pack(pady=10)
        
    def start_game(self):
        print("")
    
    def diff_set(self):
        print("")
    
    def exit_app(self):
        self.master.destroy()
    

        