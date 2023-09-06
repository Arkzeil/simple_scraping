import tkinter as tk

def update_info(update_string = ""):
    global info_area

    info_area.insert(tk.END, update_string)
    info_area.see(tk.END)

def update_process(update_string = ""):
    global progress_area

    progress_area.insert(tk.END, update_string)
    progress_area.see(tk.END)