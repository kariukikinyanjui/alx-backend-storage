#!/usr/bin/env python3
"""Inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection: A pymongo collection object
    Returns:
        ObjectId: the _id of the newly inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
