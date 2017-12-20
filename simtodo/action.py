"""
Action manager
"""

from __future__ import print_function
import config
import logger
import datastore as d

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
    task = {"name": task_name, "state": ACTIVE_STATE}

    # save task in file
    d.save_task(config.TASK_FILE_PATH, task)
    return True

def complete_task(task_name):
    """
    Mark a task as completed
    """
    logger.log("complete task: '" + task_name + "'")
    d.update_task(config.TASK_FILE_PATH, task_name, COMPLETED_STATE)
    return True

def delete_task(task_name):
    """
    Delete a task definitively
    """
    logger.log("delete task: '" + task_name + "'")
    d.delete_task(config.TASK_FILE_PATH, task_name)
    return True

PERFORM_ACTION = {
    ADD_TASK: add_task,
    COMPLETE_TASK: complete_task,
    DELETE_TASK: delete_task
}
