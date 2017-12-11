"""
Various helpers
"""

import json

def get_data_from_file(path):
    """
    Read the json file and return data
    """
    with open(path) as data_file:
        data = json.load(data_file)
    return data

def save_data_in_file(path, data):
    """
    Save the data in the json file
    """
    with open(path, "wb") as data_file:
        json.dump(data, data_file)
