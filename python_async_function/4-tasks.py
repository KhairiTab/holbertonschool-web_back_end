#!/usr/bin/env python3
"""Execute multiple coroutines"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for 'n' random delays, returning a sorted list."""
    task_wait_random(max_delay)
    delay_list = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)
