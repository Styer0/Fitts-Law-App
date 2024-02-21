import tkinter as tk

myFont = ("Consolas", 13)
class ObjForm:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        master.title("Fitts Law Game")
        master.geometry('1200x900')

        #Button to switch back to the main menu form
        back_btn = tk.Button(master, text="Quit", command=self.back_mm)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10,pady=15)
        
        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_mm)
    
    #Back to the main menu
    def back_mm(self):
        self.master.destroy()
        self.main_menu.master.deiconify()
