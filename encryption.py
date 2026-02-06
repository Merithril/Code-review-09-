from tkinter import messagebox
import tkinter as tk

def encryption(gui_root_input, gui_root_output):
    """
    Encrypts a given message stored in an tk gui object and
    sets the encrypted text to another gui's output.

    :param gui_root_input:
    :param gui_root_output:
    :return:
    """

    original_text = gui_root_input.entry_box.get("1.0", "end-1c")

    if not gui_root_input.encrypt.get():
        set_output(gui_root_output.output_box, original_text)
        return

    try:
        s = int(gui_root_input.ceaser_shift.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Encryptionshift must be a positive integer."
        )
        return

    encrypted_text = ""

    for char in original_text:

        if char.isupper():
            encrypted_text += chr((ord(char) + s - 65) % 26 + 65)

        elif char.islower():
            encrypted_text += chr((ord(char) + s - 97) % 26 + 97)

        else:
            encrypted_text += char

    set_output(gui_root_output.output_box, encrypted_text)

def set_output(text_widget, text):
    """
    Sets the output to widget from guy.

    :param text_widget:
    :param text:
    :return:
    """

    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", text)
    text_widget.config(state="disabled")