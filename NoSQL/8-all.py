#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Returns:
        List of all documents in the collection.
        Returns an empty list if no documents are found.
    """
    # Find all documents in the collection
    all_documents = mongo_collection.find()

    # Convert cursor to list of documents
    document_list = list(all_documents)

    return document_list
