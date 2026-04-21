#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with no cached datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            The dataset as a list of lists, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0.

        Returns:
            A dictionary mapping index to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """Get a page with index-based deletion-resilient pagination.

        Args:
            index: The starting index (default None, treated as 0)
            page_size: Number of items per page (default 10)

        Returns:
            A dictionary containing index-based pagination data.

        Raises:
            AssertionError: If index is out of valid range.
        """
        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < total_items, \
            "index out of range"

        data = []
        current_index = index

        while len(data) < page_size and current_index < total_items:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # Find next valid index
        next_index = current_index
        while next_index < total_items and next_index not in indexed_data:
            next_index += 1

        if next_index >= total_items:
            next_index = None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
