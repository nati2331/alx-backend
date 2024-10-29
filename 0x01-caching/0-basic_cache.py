#!/usr/bin/env python3
"""
Caching module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Creating BaseCaching Class
    """

    def put(self, key, item):
        """
        Adds to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves from cache.
        """
        return self.cache_data.get(key, None)
