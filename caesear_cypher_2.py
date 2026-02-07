"""
This module implements the ceasar cipher encryption function
to shift letters by a fixed number to generate a encryption.
"""

__author__ = "8033684, Hofmann"

from encrypted_gui_2 import caesar_encrypt


def encrypt(text: str, shift: int = 5) -> str:
    """
    Encrypts text using the caesar cipher with a specific shift value (5).
    idea for structure from ai.
    """
    results = ""
    for char in text:
        if char.isupper():
            results += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            results += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            results += char
        return results


def decrypt_function(text: str, shift: int = 5) -> str:
    """
    Decrypts a text using caesar cipher with a negative shift value.

    """

    return caesar_encrypt(text, -shift)
