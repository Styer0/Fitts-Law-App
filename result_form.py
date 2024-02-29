import tkinter as tk
from stopwatch import Stopwatch
myFont = ("Consolas", 13)

class ResultsForm:
    def __init__(self, master, obj_form, record):
        self.master = master
        self.obj_form = obj_form
        self.record = record
        
        master.title("Fitts Law Game - Results")
        master.geometry('600x400')
        
        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_obj)
        
        # Button to switch back to the trial form
        back_btn = tk.Button(master, text="Back to Trial", command=self.back_obj)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=15)

        # Display results (you can customize this based on what results you want to show)
        result_label = tk.Label(master, text="Results", font=myFont)
        result_label.pack(pady=10)
        
        record_label = tk.Label(master, text="Time: {:.2f} seconds".format(record), font=myFont)
        record_label.pack(pady=10)
    
    def back_obj(self):
        self.master.destroy()
        self.obj_form.master.deiconify()