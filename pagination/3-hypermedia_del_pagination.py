#!/usr/bin/env python3
"""
Implement deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict, Any


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
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

        if index is None:
            index = 0

        assert isinstance(page_size, int) and page_size > 0
        assert (
            isinstance(index, int)
            and 0 <= index <= max(indexed_data.keys())
        ), \
            "index out of range"

        data = []
        next_index = index
        max_index = max(indexed_data.keys())

        while len(data) < page_size and next_index <= max_index:
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        if next_index > max_index:
            next_index = None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
