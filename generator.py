"""
This module allows the user to either set a password for Tkinter by themselves or generate one using a password generator.

"""

__author__ = "8033684, Hofmann"

import string
import random

def generate_password(length: int, lower_case: bool, upper_case: bool, digits: bool) -> str :

    chars = ""
    if lower_case:
        chars += "abcdefghijklmnopqrstuvwyz"

    if upper_case:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if digits:
        chars += "0123456789"

    if not chars:
        return f"Error: please choose at least one character"

    if length <= 0:
        return f"Error: length must be at least one"

    password = "".join(random.choice(chars) for _ in range(length))
    return password





#create gitpush

if __name__ == "__main__"
    print(generate_password(1, False, False, False)