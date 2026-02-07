"""
gui generator and setup.
"""

import tkinter as tk
import password_generator

__author__ = "7155628, Keller"

def create_gui_root():
    """
    Creates the gui root and sets all things around the basic window.

    :return:
    """
    gui_root = tk.Tk()
    gui_root.title("Password Generator")
    gui_root.geometry("500x500")
    gui_root.resizable(False, False)
    return gui_root


def password_length_input(gui_root):
    """
    Sets user input to set pw length.

    :param gui_root:
    :return:
    """
    tk.Label(gui_root, text="Password Length:").pack(pady=(15, 5))
    gui_root.length_entry = tk.Entry(gui_root)
    gui_root.length_entry.pack()


def character_selection(gui_root):
    """
    Sets user input to set character selection.
    :param gui_root:
    :return:
    """
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
    """
    Setup password button to activate the generation process.
    :param gui_root:
    :return:
    """
    tk.Button(
        gui_root,
        text="Generate Password",
        command=lambda: password_generator.generate_password(gui_root)
    ).pack(pady=15)


def output_display(gui_root):
    """
    Setup output display to display the generated pw.
    :param gui_root:
    :return:
    """
    gui_root.output_var = tk.StringVar()
    tk.Label(gui_root, text="Generated Password").pack()
    tk.Entry(
        gui_root,
        textvariable=gui_root.output_var,
        width=30,
        justify="center"
    ).pack(pady=15)


def setup_gui():
    """
    Calls all the setup functions and returns the complete gui.
    :return: gui
    """
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
