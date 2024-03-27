#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_log_stats(mongo_collection):
    """Retrieve stats about Nginx logs stored in MongoDB."""
    total_logs = mongo_collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    return total_logs, method_counts, status_check_count

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    total_logs, method_counts, status_check_count = get_log_stats(nginx_collection)
