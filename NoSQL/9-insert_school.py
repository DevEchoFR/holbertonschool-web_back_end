#!/usr/bin/env python3
"""Module for inserting a new school document in MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in mongo_collection and return its _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
