"""
....

"""

__author__ = "8033684, Hofmann"

import random
import string


def generate_password(length: int, use_lowercase=True, use_uppercase=True,
                      use_digits=True, use_special_characters=True) -> str:
      if length <= 0:
          raise ValueError("length must be > 0")

      chars = ""
      if use_lowercase:
          chars += string.ascii_lowercase
      if use_uppercase:
          chars += string.ascii_uppercase
      if use_digits:
          chars += string.digits
      if use_special_characters:
          chars += string.punctuation
      if not chars:
          raise ValueError("At least one character type must be selected.")

      return "".join(random.choice(chars) for _ in range(length))