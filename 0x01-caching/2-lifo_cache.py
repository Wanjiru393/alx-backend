#!/usr/bin/python3
"""
This module contains the LIFOCache class
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """init """
        super().__init__()
        self.key = []

    def put(self, key, item):
        """
        deletes last item put in cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.key:
                self.key.remove(key)
            self.key.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                to_delete = self.key[-2]
                print("DISCARD: {}".format(to_delete))
                del self.cache_data[to_delete]
                self.key.remove(to_delete)

    def get(self, key):
        """
        returns item based on the key
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None

        return self.cache_data[key]
