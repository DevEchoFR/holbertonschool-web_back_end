# Python - Async Comprehension

This project contains exercises about asynchronous generators,
asynchronous comprehensions, and runtime measurement with asyncio.

## Files
- `0-async_generator.py` - contains an asynchronous generator that yields
  random numbers between 0 and 10 at random intervals between 0 and 10
  seconds.
- `1-async_comprehension.py` - contains an asynchronous comprehension that
  collects 10 random numbers using the asynchronous generator from
  `0-async_generator.py` and returns the list of numbers.
- `2-measure_runtime.py` - contains a function that measures the total
  runtime of the asynchronous comprehension from `1-async_comprehension.py`