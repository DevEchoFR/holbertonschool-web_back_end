#!/usr/bin/env python3
"""Module that defines an asynchronous generator of random values."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floats between 0 and 10 with one-second pauses."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
