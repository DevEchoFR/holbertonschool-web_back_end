#!/usr/bin/env python3
"""Module that defines a function to sum a list of floating-point values."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floating-point numbers in the input list."""
    return sum(input_list)
