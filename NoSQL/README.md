# NoSQL

This project introduces MongoDB and NoSQL basics through shell scripts and Python functions.

## Requirements

- Ubuntu 20.04 LTS
- MongoDB 4.4
- Python 3.9
- PyMongo 4.8.0
- pycodestyle 2.5.*

## Files

### MongoDB shell scripts

- `0-list_databases`: list all databases
- `1-use_or_create_database`: create or use `my_db`
- `2-insert`: insert one school document
- `3-all`: list all documents in `school`
- `4-match`: list documents where `name` is `Holberton school`
- `5-count`: count documents in `school`
- `6-update`: add `address` to matching documents
- `7-delete`: delete matching documents

### Python files

- `8-all.py`: list all documents in a collection
- `9-insert_school.py`: insert one document from keyword args
- `10-update_topics.py`: update topics by school name
- `11-schools_by_topic.py`: list schools by topic
- `12-log_stats.py`: print Nginx logs statistics from MongoDB
