"""
password generating function.
"""

from tkinter import messagebox
import random
import string

__author__ = "7155628, Keller"

def generate_password(gui_root):
    """
    Generates and Sets pw using gui internal values.
    :param gui_root:
    :return:
    """
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
