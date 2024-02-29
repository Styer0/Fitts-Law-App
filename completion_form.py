#completion_form.py - Ethan Nguyen
import tkinter as tk
import app_logic

myFont = ("Consolas", 20)
class completionForm:
    def __init__(self, master):
        self.master = master
        master.title("Fitts Law Experiment - End")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}+0+0")
        
        word_label = tk.Label(master, text="Thank you for your contribution!", font=myFont)
        word_label.pack(pady=20)
        
        my_name_label = tk.Label(master, text="This program was created by: Ethan Nguyen", font=myFont)
        my_name_label.pack(pady=20)
        
        exit_btn = tk.Button(master, text="Quit", command=self.exitApp)
        exit_btn['font'] = myFont
        exit_btn.pack(pady=15)
        
        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.exitApp)
    
    def exitApp(self):
         app_logic.stop_program()
