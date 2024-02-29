#app_logic.py -Ethan Nguyen
def set_forms(root, main_menu, obj_form, results_form, completion_form):
    global root_global, main_menu_global, obj_form_global, results_form_global, completion_form_global
    root_global = root
    main_menu_global = main_menu
    obj_form_global = obj_form
    results_form_global = results_form
    completion_form_global = completion_form

# Stops all the programs and windows from running
def stop_program():
    if root_global:
        root_global.destroy()
    if obj_form_global:
        obj_form_global.destroy()
    if results_form_global:
        results_form_global.destroy()
    if completion_form_global:
        completion_form_global.destroy()