#!/usr/bin/env python3
"""Writing strings to Redis, Reading from Redis and recovering original type,
   Incrementing values, Storing lists, Retrieving lists"""
from typing import Union, Any
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
