#!/usr/bin/env python3
"""Module containing index_range function and server class"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range function

    Args:
        page (int): [Number of page]
        page_size (int): [Number of page size]

    Returns:
        Tuple[int, int]: [Tuple with two values]
    """
    my_page = page_size * (page - 1)
    my_page_size = page * page_size
    return my_page, my_page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to get a page
        """
        try:
            assert(type(page) == int) 
            assert(type(page_size) == int)
        except AssertionError:
            raise AssertionError()

        try:
            assert(page > 0)
            assert(page_size > 0)
        except AssertionError:
            raise AssertionError()

        index = index_range(page, page_size)
        self.dataset()
        my_list = []

        for i in range(index[0], index[1]):
            try:
                my_list.append(self.__dataset[i])
            except IndexError:
                return []
        return my_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hyper page
        """
        data = self.get_page(page, page_size)
        size = len(data)

        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page >= 3000:
            next_page = None
        else:
            next_page = page + 1

        total = math.ceil(len(self.dataset()) / page_size)

        my_dict = {
            "page_size": size,
            "page": page,
            "data": data,
            "next_size": next_page,
            "prev_page": prev_page,
            "total_pages": total
        }

        return my_dict
