#!/usr/bin/env python3
"""Cache management using Redis in Python"""
import redis
import uuid
from typing import Union


class Cache:
    """A class for managing a cache using Redis"""

    def __init__(self):
        """
        Initialize the Cache object by creating an instance of the Redis
        clinet and flushing the Redis database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache and return a unique key for accessing
        the stored data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
