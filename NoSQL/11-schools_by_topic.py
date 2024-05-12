#!/usr/bin/env python3
"""
    Returns the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):

    """   Returns:
        A list of dictionaries representing schools having the specific topic.
    """
    collection = mongo_collection.find({"topic": topic})
    return list(collection)
