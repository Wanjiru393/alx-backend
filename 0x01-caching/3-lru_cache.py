#!/usr/bin/pthon3
"""
This module contains the LRUCache module
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ the LRUCache class inherits
    from BaseCaching"""

    def __init__(self):
        """ Init function for the LRUCache.
        """
        super().__init__()
        self.key = []

    def put(self, key, item):
        """ put function
        Args: key and item  to add to the dict
        """
        if key and item:

            if key in self.key:
                self.key.remove(key)
            self.key.append(key)

            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                to_discard = self.key[0]
                print("DISCARD: {}".format(to_discard))
                del self.cache_data[to_discard]
                self.key.remove(to_discard)

    def get(self, key):
        """
        Returns the item based on the key
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None

        self.key.remove(key)
        self.key.append(key)

        return self.cache_data[key]
