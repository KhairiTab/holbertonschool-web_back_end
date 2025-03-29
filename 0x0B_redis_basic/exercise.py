#!/usr/bin/env python3
"""Writing strings to Redis, Reading from Redis and recovering original type,
   Incrementing values, Storing lists, Retrieving lists"""
from typing import Union, Callable, Optional, Any
import redis
import uuid


class Cache:
    """Cache class to interact with Redis."""

    def __init__(self) -> None:
        """Constructor - store an instance of the
        Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key,
        store the input data in Redis, and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable[[bytes], Any]] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis using a key
        and optionally apply a conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve and decode data from Redis as a string."""
        data = self._redis.get(key)
        return data.decode("utf-8") if data else None

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve and decode data from Redis as an integer."""
        data = self._redis.get(key)
        if data is None:
            return None
        try:
            return int(data.decode("utf-8"))
        except (ValueError, AttributeError):
            return 0
