#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator function that yields
    random numbers with a 1-second delay."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
