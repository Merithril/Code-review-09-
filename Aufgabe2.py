import tkinter as tk
from tkinter import messagebox


def setup_gui():
    input_gui = setup_input_gui()
    output_gui = setup_output_gui(input_gui)

    tk.Button(
        input_gui,
        text="Output Message",
        command=lambda: encryption(input_gui, output_gui)
    ).pack(pady=15)

    return input_gui, output_gui


def setup_input_gui():
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

    gui_root.ceaser_shift = tk.Entry(gui_root, width=3)
    gui_root.ceaser_shift.pack(pady=(10, 10))

    return gui_root


def setup_output_gui():

    gui_root = tk.Toplevel()
    gui_root.title("Ausgabe Fenster")
    gui_root.geometry("500x500")
    gui_root.resizable(False, False)

    tk.Label(gui_root, text="Ausgegebene Nachricht").pack()

    gui_root.output_box = tk.Text(gui_root, height=10, width=50)
    gui_root.output_box.pack()

    gui_root.output_box.config(state="disabled")

    return gui_root


def set_output(text_widget, text):
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", text)
    text_widget.config(state="disabled")


def encryption(gui_root_input, gui_root_output):

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


def main():
    gui_in, gui_out = setup_gui()
    gui_in.mainloop()


if __name__ == "__main__":
    main()
