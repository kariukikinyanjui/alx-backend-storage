#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    return list[entry for entry in mongo_collection.find()]
