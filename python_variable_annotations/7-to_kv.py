#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Tuple, Union


def to_key(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:

    """Takes a string `k` and an int or float `v` as arguments
    Returns a tuple containing `k` and the square of `v`
    annotated as a float."""
    return k, float(v) ** 2
