#!/usr/bin/python3
"""
This module contains the MRUcache module
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.key = []

    def put(self, key, item):
        """
        Adds key value items to a dictionary
        """
        if key and item:
            if key in self.key:
                self.key.remove(key)
            self.key.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                to_discard = self.key[-2]
                print("DISCARD: {}".format(to_discard))
                del self.cache_data[to_discard]

    def get(self, key):
        """
        Returns the item based on the key provided
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None

        self.key.remove(key)
        self.key.append(key)
        return self.cache_data[key]
