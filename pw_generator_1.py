"""
This module contains the core function to generate a random password
using the user input for length and character specification.

"""

__author__ = "8033684, Hofmann"

import random


def generate_password(length: int, chars: str) -> str:
    """
    Generates a random password based on selected character options and
    user specific length.

    """
    if length <= 0:
        raise ValueError("length must be > 0")

    if not chars:
        raise ValueError("At least one character type must be selected.")

    return "".join(random.choice(chars) for _ in range(length))
