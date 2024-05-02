#!/usr/bin/env python3
"""duck type an iterable object"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:

    """
    Takes a list of strings `lst` as input
    Returns a list of tuples where each tuple contains
    an element of `lst` and its length
    """
    return [(i, len(i)) for i in lst]
