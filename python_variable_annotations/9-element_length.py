#!/usr/bin/env python3
"""Module that defines a function to pair elements with their lengths."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Return tuples pairing each element with its length."""
    return [(i, len(i)) for i in lst]
