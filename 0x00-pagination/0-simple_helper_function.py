#!/usr/bin/env python3
def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page size.

    Parameters:
    - page (int): Page number (1-indexed).
    - page_size (int): Number of items per page.

    Returns:
    - Tuple of size two: (start_index, end_index).
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index

page_number = 3
items_per_page = 10
start, end = index_range(page_number, items_per_page)

print(f"For page {page_number}, the start index is {start} and the end index is {end}.")
