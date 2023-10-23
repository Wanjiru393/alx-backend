#!/usr/bin/env python3
"""This module defines the function `index_range`"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """
    return (page_size * page - page_size, page_size * page)


if __name__ == "__main__":
    print("(1, 7) =>", index_range(1, 7))
    print("(3, 15) =>", index_range(3, 15))
    print("(1, 1) =>", index_range(1, 1))
