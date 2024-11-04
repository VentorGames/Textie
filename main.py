import tkinter as tk
from tkinter import Menu, Text, Scrollbar, filedialog
import os


root = tk.Tk()
root.title("Textie")
root.geometry("800x800")


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Wis de huidige inhoud
            text_area.insert(tk.END, content)
        root.title(f"Textie - {os.path.basename(file_path)}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        root.title(f"Textie - {os.path.basename(file_path)}")


def dark_mode():
    text_area.config(
        fg="blue",
        bg="gray"
    )

def light_mode():
    text_area.config(
        fg="black",
        bg="white"
    )

def proggraming_mode():
    text_area.config(
        fg="white",
        bg="black"
    )

def drake_mode():
    text_area.config(
        fg="white",
        bg="white"
    )




text_area = Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill="both", padx=10, pady=10)

menubar = Menu(root)
bestand_menu = Menu(menubar, tearoff=0)
bestand_menu.add_command(label="Open", command=open_file)
bestand_menu.add_command(label="Save", command=save_file)
bestand_menu.add_separator()
bestand_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=bestand_menu)

settings_menu = Menu(menubar, tearoff=0)
settings_menu.add_command(label="Dark Mode", command=dark_mode)
settings_menu.add_command(label="Light Mode", command=light_mode)
settings_menu.add_command(label="Proggraming Mode", command=proggraming_mode)
settings_menu.add_command(label="Drake's mode", command=drake_mode)
menubar.add_cascade(label="Settings", menu=settings_menu)




root.config(menu=menubar)
root.mainloop()