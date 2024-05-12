#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """

    return mongo_collection.find()
