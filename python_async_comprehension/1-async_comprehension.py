#!/usr/bin/env python3
"""Module that defines an asynchronous comprehension coroutine."""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect and return ten random floats from async_generator."""
    return [value async for value in async_generator()]
