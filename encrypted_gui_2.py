"""
....
"""

__author__ = "8033684, Hofmann"

import tkinter as tk
from operator import index
from tkinter import messagebox
from tkinter import scrolledtext
from caesear_cypher_2 import caesar_encrypt

def main():
    encryption = Caesar_cypher_encrypt()
    encryption.call()

class Caesar_cypher_encrypt:
    def __init__(self):
        self.input = None
        self.output = None

    def  call (self):
        self.create_input_window()
        self.create_output_window()
        self.input.mainloop()   #input or root.1


    def create_input_window(self):
        self.input = tk.Tk()
        self.input.title("Input Window")
        self.input.geometry("500x500")

        #Label
        tk.Label(self.input, text="Enter Text:").pack(pady=10)
        self.input_text = scrolledtext.ScrolledText(self.input, height=10, width= 30)
        self.input_text.pack(pady=10)

        # button
        tk.Button(self.input,
                  text="Encrypt",
                  command=self.call).pack(pady=15)

        #checkbox
        self.encrypt_variable = tk.BooleanVar(value = False)
        (tk.Checkbutton(self.input,
                       text=("Encryption with Caesar"),
                       variable = self.encrypt_variable
                        ).pack(pady=10))


        # shift Input
        tk.Label(self.input, text="Input (Standard: 5").pack()
        self.shift_entry = tk.Entry(self.input)
        self.shift_entry.insert(0, "5")
        self.shift_entry.pack(pady=5)


    def create_output_window(self):
        self.output = tk.Tk()
        self.output.title("Output Window")
        self.output.geometry("500x500")

        #Label
        tk.Label(self.output, text="received messages").pack(pady=10)
        self.output_text = scrolledtext.ScrolledText(self.output, height=10, width= 30)
        self.output_text.pack(pady=10, padx=20, fill=tk.BOTH, expand= True)

    def messager (self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showerror("Error", "Please enter a message")
                return

            shift = int(self.shift_entry.get())

            if self.encrypt_variable.get():
                message = caesar_encrypt(text, shift)
            else:
                message = text

            self.input_text.delete("1.0", tk.END)
            self.output_text.delete("1.0", tk.END)

        except ValueError:
            messagebox.showerror("Error. Please enter a digit for shift")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()


