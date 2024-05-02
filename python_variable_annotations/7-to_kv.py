#!/usr/bin/env python3
"""Takes a string `k` and an int or float `v` as arguments"""
from typing import Tuple, Union


def to_key(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:

    """Returns a tuple containing `k` and the square of `v`
    annotated as a float."""
    return k, float(v ** 2)
