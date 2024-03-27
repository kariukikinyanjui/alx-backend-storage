#!/usr/bin/env python3
"""Cache management using Redis in Python"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieve data from the cache using the given key and optionally
        apply a conversion function
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve a string value from the cache using the given key"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve an integer value from the cache using the given value"""
        return self.get(key, fn=int)
