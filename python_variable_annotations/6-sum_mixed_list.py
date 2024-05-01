#!/usr/bin/env python3
"""
    Calculate the sum of a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lsd: List[Union[int, float]]) -> float:

    """Returns:
    float: The sum of the elements in the input list.
    """
    return sum(mxd_lsd)
