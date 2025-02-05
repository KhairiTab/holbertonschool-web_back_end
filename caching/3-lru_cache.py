#!/usr/bin/python3
""" LRU caching system """

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()  # Maintain insertion & access order

    def put(self, key, item):
        """ Add an item to the cache with LRU eviction policy """
        if key is None or item is None:
            return
        # If key exists, move it to the end (most recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item  # Insert or update the key
        # If cache exceeds the limit, remove the LRU item (first one)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", lru_key)

    def get(self, key):
        """ Retrieve an item from the cache and update usage order """
        if key is None or key not in self.cache_data:
            return None
        # Move accessed key to the end to mark as most recently used
        self.cache_data.move_to_end(key)

        return self.cache_data[key]
