import tkinter as tk
from tkinter import messagebox
import random
import string


def create_gui_root():
    gui_root = tk.Tk()
    gui_root.title("Password Generator")
    gui_root.geometry("500x500")
    gui_root.resizable(False, False)
    return gui_root


def password_length_input(gui_root):
    tk.Label(gui_root, text="Password Length:").pack(pady=(15, 5))
    gui_root.length_entry = tk.Entry(gui_root)
    gui_root.length_entry.pack()


def character_selection(gui_root):
    tk.Label(gui_root, text="Character Selection:").pack(pady=(15, 5))

    options = {
        "lower": ("Lowercase (a-z)", True),
        "upper": ("Uppercase (A-Z)", True),
        "digits": ("Digits (0-9)", True),
        "symbols": ("Special Symbols (!@#$%^&*)", False)
    }

    gui_root.char_options = {}

    for key, (text, default) in options.items():
        var = tk.BooleanVar(value=default)
        gui_root.char_options[key] = var
        tk.Checkbutton(gui_root, text=text, variable=var).pack()

def generate_password_button(gui_root):
    tk.Button(
        gui_root,
        text="Generate Password",
        command=lambda: generate_password(gui_root)
    ).pack(pady=15)


def output_display(gui_root):
    gui_root.output_var = tk.StringVar()
    tk.Label(gui_root, text="Generated Password").pack()
    tk.Entry(
        gui_root,
        textvariable=gui_root.output_var,
        width=30,
        justify="center"
    ).pack(pady=15)


def generate_password(gui_root):
    try:
        pw_length = int(gui_root.length_entry.get())
        if pw_length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Password length must be a positive integer."
        )
        return

    pool = ""
    if gui_root.char_options["lower"].get():
        pool += string.ascii_lowercase
    if gui_root.char_options["upper"].get():
        pool += string.ascii_uppercase
    if gui_root.char_options["digits"].get():
        pool += string.digits
    if gui_root.char_options["symbols"].get():
        pool += string.punctuation

    if not pool:
        messagebox.showerror(
            "Selection Error", "Select at least one character type.")
        return

    password = "".join(random.choice(pool) for _ in range(pw_length))
    gui_root.output_var.set(password)


def setup_gui():
    gui = create_gui_root()
    password_length_input(gui)
    character_selection(gui)
    generate_password_button(gui)
    output_display(gui)
    return gui


def main():
    gui = setup_gui()
    gui.mainloop()


if __name__ == "__main__":
    main()
