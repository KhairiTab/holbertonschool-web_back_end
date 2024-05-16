#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random


async def async_generator():
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)

        # Generate a random number between 0 and 10
        random_number = random.uniform(0, 10)

        # Yield the random number
        yield random_number
