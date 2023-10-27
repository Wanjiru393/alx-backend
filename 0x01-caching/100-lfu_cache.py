#!/bin/env/python3
"""LFUCache"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    """

    def __init__(self):
        """
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        """
        if key and item:
            self.cache_data[key] = item

        if key in self.keys:
            self.keys.remove(key)

        self.keys.append(key)

        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_discard = self.keys[0]
                print("DISCARD: ", to_discard)
                self.keys.remove(key)

    def get(self, key):
        if key is None:
            return None
        if key not in self.cache_data:
            return None

        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
