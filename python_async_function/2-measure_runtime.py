#!/usr/bin/env python3
"""Module that defines a function to measure coroutine runtime."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure average runtime per coroutine for wait_n(n, max_delay)."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
