"""
User interface of the password generator, enables user input.
"""

__author__ = "8033684, Hofmann"

import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_password

if __name__ == "__main__":
    root = tk.Tk()
    root.title("password_generator")
    root.geometry("300x300")

    button = tk.Button(
        root,
        text= "Please press to generate a password",
        command= generate_password
    )
    button.pack()
    root.mainloop()
    return root

def label():
    label = tk.Label(root, text="Please press to generate a password")
    label.pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

def buttons():
    button = tk.Button(root, text="Generate a password")
    button.pack()
    var_lower = tk.IntVar(value= 1)
    var_upper = tk.IntVar(value = 1)
    var_digit = tk.IntVar(value = 1)

def generator():
    try:
        length = it(length_etry.get())
    except ValueError:
        messagebox.showerror("Error", "Length must be an integer")
        return generator()

    lower_case = var_lower.get() == 1
    upper_case = var_upper.get() == 1
    digits = var_digits.get() == 1

    password = generate_password(length, lower_case, upper_case, digits)
