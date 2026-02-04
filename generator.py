"""
This module allows the user to either set a password for Tkinter by themselves or generate one using a password generator.

"""

__author__ = "8033684, Hofmann"

import random
import string
import tkinter as tk
from tkinter import messagebox

def main():
    """

    """
    gui = gui.root
    gui.mainloop()

def gui_root():
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("300x300")
    return root

def gui_button():
    tk.Button(
        root,
        text="Generate a password",
        command = generate_password(root)
    ).pack(pady=5)

def generate_password():
    try:
        length = int(root,length_input.get())
        if length <= 0:
            raise ValueError("Length must be greater than 0. Please try again.")
        return

def possible_characters(legnth: int, use_lower_case: bool, use_upper_case: bool, digits: bool) -> str:
    chars = ""
    if use_lower_case:
        chars += string.ascii_lowercase
    if use_upper_case:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if not chars:
        return "Error: please choose at least one character."

    password = (".join(random.choice(chars) for _ in range(length))")
    return password

def length_input():


if __name__ == "__main__":
    main()