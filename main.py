#main.py - Ethan Nguyen
import tkinter as tk
from main_menu import MainMenu
import app_logic

root_global = None
main_menu_global = None
obj_form_global = None
results_form_global = None
completion_form_global = None

def create_root():
    global root_global
    root_global = tk.Tk()
    root_global.title("Fitts Law Experiment")

def create_main_menu():
    global main_menu_global
    main_menu_global = MainMenu(root_global)

def run_application():
    create_root()
    create_main_menu()
    app_logic.set_forms(root_global, main_menu_global, obj_form_global, results_form_global, completion_form_global)
    root_global.mainloop()

if __name__ == "__main__":
    run_application()
