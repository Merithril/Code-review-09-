"""
This module allows the user to either set a password for Tkinter by themselves or generate one using a password generator.

"""

__author__ = "8033684, Hofmann"

import tkinter as tk
from tkinter import messagebox
from pw_generator_1 import generate_password
import string
import random

def main():
    """

    """
    gui = gui_root()
    gui.mainloop()

def gui_root():
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("500x600")
    length_input(root)
    possible_characters(root)
    gui_pw_button(root)
    output_display(root)
    return root


def length_input(gui_root):
    tk.Label(gui_root,
            text="Please enter the length of the password.").pack(pady=(15, 5))
    gui_root.length_input = tk.Entry(gui_root)
    gui_root.length_input.pack()

def possible_characters(gui_root):
    tk.Label(gui_root,
             text= "Please choose a character from the following possibilities:").pack(pady=5)
    gui_root.char_options = {}
    use_lower_case = tk.BooleanVar(value=True)
    use_upper_case = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_special_characters = tk.BooleanVar(value=True)

    gui_root.char_options["lowercase"] = use_lower_case
    gui_root.char_options["uppercase"] = use_upper_case
    gui_root.char_options["digits"] = use_digits
    gui_root.char_options["special_characters"] = use_special_characters


    tk.Checkbutton(gui_root,
                   text = "lower case characters: ",
                   variable = use_lower_case).pack()
    tk.Checkbutton(gui_root,
                   text = "upper case characters: ",
                   variable = use_upper_case).pack()
    tk.Checkbutton(gui_root,
                   text = "digits: ",
                   variable = use_digits).pack()
    tk.Checkbutton(gui_root,
                   text = "special characters: ",
                   variable = use_special_characters).pack()


def output_display(gui_root):
        gui_root.output_var = tk.StringVar()
        tk.Label(gui_root,
                 text="customized password:").pack()
        tk.Entry(gui_root,
                 textvariable=gui_root.output_var).pack(pady=15)

def generate_pw_gui(gui_root):
    chars = ""
    if gui_root.char_options["lowercase"].get():
        chars += string.ascii_lowercase
    if gui_root.char_options["uppercase"].get():
        chars += string.ascii_uppercase
    if gui_root.char_options["digits"].get():
        chars += string.digits
    if gui_root.char_options["special_characters"].get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error")
        #return "Error: please choose at least one character."

    try:
        length = int(gui_root.length_input.get())
        pw = generate_password(length, chars)
        gui_root.output_var.set(pw)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def gui_pw_button(gui_root):
    tk.Button(
        gui_root,
        text="Generate Password",
        command=lambda r=gui_root: generate_pw_gui(r)
    ).pack(pady=50)



if __name__ == "__main__":
            main()
