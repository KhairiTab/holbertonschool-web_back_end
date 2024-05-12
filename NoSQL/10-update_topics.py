#!/usr/bin/env python3
"""
    Changes all topics of a school document based on the name."""


def update_topics(mongo_collection, name, topics):

    """
name (string): The school name to update.
        topics (list of strings): The list of topics approached in the school.

    Returns:
        The number of documents updated.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
