# result_form.py
import tkinter as tk
from stopwatch import Stopwatch

myFont = ("Consolas", 13)

class ResultsForm:
    def __init__(self, master, obj_form, recorded_time, click_timestamps):
        self.master = master
        self.obj_form = obj_form
        self.recorded_time = recorded_time
        self.click_timestamps = click_timestamps

        master.title("Fitts Law Game - Results")
        master.geometry('600x400')

        # Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_obj)

        # Button to switch back to the trial form
        back_btn = tk.Button(master, text="Back to Trial", command=self.back_obj)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=15)

        # Display results
        result_label = tk.Label(master, text="Results", font=myFont)
        result_label.pack(pady=10)
        
        # Display time intervals between clicks
        intervals_label = tk.Label(master, text="Time Intervals:", font=myFont)
        intervals_label.pack(pady=10)

        for i in range(1, len(self.click_timestamps)):
            time_interval = self.click_timestamps[i] - self.click_timestamps[i - 1]
            interval_label = tk.Label(master, text=f"{i}-{i+1}. {time_interval:.2f} seconds", font=myFont)
            interval_label.pack()

        # Display recorded time
        recorded_time_label = tk.Label(master, text=f"Recorded Time: {recorded_time:.2f} seconds", font=myFont)
        recorded_time_label.pack(pady=10)

    def back_obj(self):
        self.master.destroy()
        self.obj_form.master.deiconify()
