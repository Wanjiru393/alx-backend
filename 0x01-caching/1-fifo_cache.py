#!/usr/bin/env python3
"""
This module contains FIFOCache
It uses FIFO caching strategy
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOClass """

    def __init__(self):
        """ init the FIFOClass """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Deletes if cache_data is greater than Max_ITEMS """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            to_discard = self.order[0]
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]
            self.order.pop(0)

    def get(self, key):
        """ get the item based on the key """
        if key is None:
            return None
        elif key not in self.cache_data:
            return None
        return self.cache_data[key]
