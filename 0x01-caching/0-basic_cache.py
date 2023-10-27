#!/usr/bin/env python3
"""
Module contains the BasicCache that inherits from BaseCaching
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits fro BaseCaching
    """

    def __init__(self):
        """ initializing base_caching"""
        super().__init__()

    def put(self, key, item):
        """
        Stores key value in self.cache_data
        Args: key - key for self.cache_data dict
        item- value for the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves items based on key
        Args: key - key used for retrieval
        return item based on the key
        """
        if key is None:
            return None
        elif key not in self.cache_data:
            return None
        return self.cache_data[key]
