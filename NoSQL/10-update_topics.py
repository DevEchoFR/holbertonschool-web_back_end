#!/usr/bin/env python3
"""Module for updating school topics in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """Update all topics of the school document matching name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
