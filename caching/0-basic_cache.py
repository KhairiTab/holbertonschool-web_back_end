#!/usr/bin/env python3
"""
BaseCaching module representing how to save data and
manipulate it from the cache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' A basic cache.
        Inherits from class BaseCaching.
        Attributes:
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache
    '''

    def put(self, key, item):
        ''' Add key/value pair to cache.
        If either `key` or `item` is None, do nothing. '''
        if (key is None or item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' Return value stored in `key` of cache.
        If key is None or does not exist in cache, return None. '''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
