#!/usr/bin/env python3
"""Module that defines a function to sum integers and floats in a list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all integer and floating-point values as a float."""
    return float(sum(mxd_lst))
