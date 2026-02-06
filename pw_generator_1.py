"""
....

"""

__author__ = "8033684, Hofmann"

import random
import string


def generate_password(length: int, chars: str) -> str:
      if length <= 0:
          raise ValueError("length must be > 0")

      if not chars:
          raise ValueError("At least one character type must be selected.")

      return "".join(random.choice(chars) for _ in range(length))