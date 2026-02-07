"""
setup for gui for excersise 2 requirements
"""

import tkinter as tk
import encryption

__author__ = "7155628, Keller"


def setup_gui():
    """
    Setup both GUIs for the program. Also sets Button functionality
    between the two Windows.

    :return: input_gui, output_gui
    """

    input_gui = setup_input_gui()
    output_gui = setup_output_gui()

    tk.Button(
        input_gui,
        text="Output Message",
        command=lambda: encryption.encryption(input_gui, output_gui)
    ).pack(pady=15)

    return input_gui, output_gui


def setup_input_gui():
    """
    Creates the input guy for user interaction.

    :return: gui_root
    """

    gui_root = tk.Tk()
    gui_root.title("Eingabe Fenster")
    gui_root.geometry("500x500")
    gui_root.resizable(False, False)

    tk.Label(gui_root, text="Nachricht eingeben").pack()

    gui_root.entry_box = tk.Text(gui_root, height=10, width=50)
    gui_root.entry_box.pack(pady=(10, 10))

    gui_root.encrypt = tk.BooleanVar(value=False)
    tk.Checkbutton(
        gui_root,
        text="Verschlüsseln",
        variable=gui_root.encrypt
    ).pack()

    tk.Label(gui_root, text="Cesarencryption shift eingeben.").pack()
    gui_root.ceaser_shift = tk.Entry(gui_root, width=3)
    gui_root.ceaser_shift.pack(pady=(10, 10))

    return gui_root


def setup_output_gui():
    """
    Sets up the output window displaying the encrypted text.

    :return: gui_root
    """
    gui_root = tk.Toplevel()
    gui_root.title("Ausgabe Fenster")
    gui_root.geometry("500x500")
    gui_root.resizable(False, False)

    tk.Label(gui_root, text="Ausgegebene Nachricht").pack()

    gui_root.output_box = tk.Text(gui_root, height=10, width=50)
    gui_root.output_box.pack()

    gui_root.output_box.config(state="disabled")

    return gui_root


def main():
    gui_in, gui_out = setup_gui()
    gui_in.mainloop()


if __name__ == "__main__":
    main()
