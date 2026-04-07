#!/usr/bin/env python3
"""Module that defines a coroutine returning a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay up to max_delay seconds and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
