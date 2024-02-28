import tkinter as tk
from obj_form import ObjForm

myFont = ("Consolas", 20)
class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Fitts Law Experiment!")
        master.geometry('1200x900')
        
        title_label = tk.Label(master, text="Fitts Law Experiment!", font=myFont)
        title_label.pack(pady=150)

        start_btn = tk.Button(master, text="Start", command=self.start_game)
        start_btn['font'] = myFont
        start_btn.pack(pady=25)

        exit_btn = tk.Button(master, text="Exit", command=self.exit_app)
        exit_btn['font'] = myFont
        exit_btn.pack(pady=25)
    
    #start the fitts law trial
    def start_game(self):
        self.obj_form = tk.Toplevel(self.master)
        self.master.withdraw()
        ObjForm(self.obj_form, self)
    
    #exit the program
    def exit_app(self):
        self.master.destroy()
    

        