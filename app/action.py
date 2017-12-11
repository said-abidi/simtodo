"""
Action manager
"""

from __future__ import print_function
import json
import config
import logger
import helper as h

SEPARATOR = "==>"

ADD_TASK = "ADD"
COMPLETE_TASK = "COMPLETE"
DELETE_TASK = "DELETE"

ACTIVE_STATE = "active"
COMPLETED_STATE = "completed"

def add_task(task_name):
    """
    Add task to json file
    """
    logger.log("add task to json file: '" + task_name + "'")
    data = h.get_data_from_file(config.TASK_FILE_PATH)

    data["tasks"].append({
        "title": task_name,
        "state": ACTIVE_STATE
    })

    # save task in file
    h.save_data_in_file(config.TASK_FILE_PATH, data)
    return True

def complete_task(task_name):
    """
    Mark a task as completed
    """
    logger.log("complete task: '" + task_name + "'")
    data = h.get_data_from_file(config.TASK_FILE_PATH)

    found = False
    for task in data["tasks"]:
        if task["title"] == task_name:
            task["state"] = COMPLETED_STATE
            found = True
            break

    # save task in file
    h.save_data_in_file(config.TASK_FILE_PATH, data)
    return found

def delete_task(task_name):
    """
    Delete a task definitively
    """
    logger.log("delete task: '" + task_name + "'")
    data = h.get_data_from_file(config.TASK_FILE_PATH)

    found = False
    task_to_be_deleted = None
    for task in data["tasks"]:
        if task["title"] == task_name:
            task_to_be_deleted = task
            found = True
            break
    data["tasks"].remove(task_to_be_deleted)

    # save task in file
    h.save_data_in_file(config.TASK_FILE_PATH, data)
    return found

PERFORM_ACTION = {
    ADD_TASK: add_task,
    COMPLETE_TASK: complete_task,
    DELETE_TASK: delete_task
}
