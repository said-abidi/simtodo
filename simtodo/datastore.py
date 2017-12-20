"""
Various helpers around datastore
"""

from tinydb import TinyDB, Query

def get_data(path):
    """
    Read the json file with TinyDB and return data
    """
    tiny_db = TinyDB(path)
    return tiny_db.all()

def update_task(path, taskname, state):
    """
    Update the state of the task
    """
    tiny_db = TinyDB(path)
    task = Query()
    tiny_db.update({'state': state}, task.name == taskname)

def save_task(path, task):
    """
    Save the data in the json file using TinyDB
    """
    tiny_db = TinyDB(path)
    tiny_db.insert(task)

def delete_task(path, taskname):
    """
    Delete a task
    """
    tiny_db = TinyDB(path)
    task = Query()
    tiny_db.remove(task.name == taskname)
