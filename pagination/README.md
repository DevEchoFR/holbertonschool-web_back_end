# Pagination Project

This project implements various pagination strategies for REST APIs, including simple page-based pagination, hypermedia pagination with metadata, and deletion-resilient pagination.

## Learning Objectives

By completing this project, you will understand:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata (HATEOAS)
- How to paginate in a deletion-resilient manner

## Project Structure

### Task 0: Simple Helper Function
**File:** `0-simple_helper_function.py`

Implements the `index_range` function that calculates the start and end indexes for a given page and page size.

```python
from 0-simple_helper_function import index_range

# Returns (0, 7) for page 1 with page_size 7
index_range(1, 7)

# Returns (30, 45) for page 3 with page_size 15
index_range(page=3, page_size=15)
```

### Task 1: Simple Pagination
**File:** `1-simple_pagination.py`

Implements the `Server` class with a `get_page` method that retrieves a specific page from a CSV dataset.

```python
from 1-simple_pagination import Server

server = Server()
page_data = server.get_page(1, 10)  # First page with 10 items
```

**Features:**
- Validates that page and page_size are positive integers
- Returns empty list if requested page is out of range
- Caches the dataset for performance

### Task 2: Hypermedia Pagination
**File:** `2-hypermedia_pagination.py`

Extends the `Server` class with a `get_hyper` method that returns pagination metadata along with the data.

```python
from 2-hypermedia_pagination import Server

server = Server()
result = server.get_hyper(1, 10)
# Returns:
# {
#   'page_size': 10,
#   'page': 1,
#   'data': [...],
#   'next_page': 2,
#   'prev_page': None,
#   'total_pages': 1942
# }
```

**Metadata Included:**
- `page_size`: Number of items on the current page
- `page`: Current page number
- `data`: The actual page data
- `next_page`: Next page number or None if on last page
- `prev_page`: Previous page number or None if on first page
- `total_pages`: Total number of pages in the dataset

### Task 3: Deletion-Resilient Hypermedia Pagination
**File:** `3-hypermedia_del_pagination.py`

Implements an index-based pagination system that is resilient to dataset deletions.

```python
from 3-hypermedia_del_pagination import Server

server = Server()
result = server.get_hyper_index(0, 10)
# Returns:
# {
#   'index': 0,
#   'data': [...],
#   'page_size': 10,
#   'next_index': 10
# }
```

**Features:**
- Uses an indexed dataset to handle deletions gracefully
- If items are deleted between queries, users won't miss entries when navigating pages
- Returns the actual starting index and next index to query

## Dataset

The project uses the `Popular_Baby_Names.csv` file containing baby name statistics with the following columns:
- Year of Birth
- Gender
- Ethnicity
- Child's First Name
- Count
- Rank

## Requirements

- Python 3.9+
- All files follow PEP 8 style (pycodestyle 2.5.*)
- All functions have proper type annotations
- All modules and functions have documentation strings
- Each file starts with `#!/usr/bin/env python3`

## Running the Tests

```bash
# Test Task 0
python3 0-main.py

# Test Task 1
python3 1-main.py

# Test Task 2
python3 2-main.py

# Test Task 3
python3 3-main.py
```

## API Usage Examples

### Simple Pagination
```python
server = Server()
first_page = server.get_page(1, 10)  # First 10 items
second_page = server.get_page(2, 10)  # Items 11-20
```

### Hypermedia Pagination
```python
server = Server()
response = server.get_hyper(1, 10)
# Client can see total_pages and navigate accordingly
if response['next_page']:
    next_response = server.get_hyper(response['next_page'], 10)
```

### Deletion-Resilient Pagination
```python
server = Server()
first = server.get_hyper_index(0, 10)
# Even if items are deleted, querying next_index will get the next 10 available items
second = server.get_hyper_index(first['next_index'], 10)
```

## Author

Created as part of the Holberton School Web Back-End curriculum.
