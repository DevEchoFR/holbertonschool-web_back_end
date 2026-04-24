#!/usr/bin/env python3
"""Module for finding schools by topic in MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that include the given topic."""
    return list(mongo_collection.find({"topics": topic}))
