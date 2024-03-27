#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: a pymongo collection object
        topic(str): the topic to search

    Returns:
        list: a list of schools that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
