"""
....
"""

__author__ = "8033684, Hofmann"

import random
import string

from ai import caesar_encrypt


def encrypt(text: str, shift: int = 5) -> str:
    results = ""
    for char in text:
        if char.isupper():
            results += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            results += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            results += char
        return results

def  decrypt_function(text: str, shift: int = 5) -> str:
    return caesar_encrypt(text, -shift)
