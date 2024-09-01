#!/usr/bin/env

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a page of a list.

    :param page: The current page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

