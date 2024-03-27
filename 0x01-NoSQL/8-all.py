#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Args:
        mongo_collection: A Pymongo collection object

    Returns:
        list: A list containing all documents in the collection
    """
    return [entry for entry in mongo_collection.find()]
