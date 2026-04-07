#!/usr/bin/env python3
"""Module that defines a function returning a key and squared numeric value."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the key and the squared numeric input value."""
    return (k, float(v ** 2))
