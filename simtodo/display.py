"""
Display results in Alfred
"""

from __future__ import print_function
import json
import parser
import datastore as d
import logger
import config
import action as a
import icon as i

def display(query):
    """
    Display results by parsing argument
    Display tasklist if no argument given and add option if argument is present
    """
    results = []
    if query.replace(" ", "") == "":
        logger.log("display task list")
        task_list = d.get_data(config.TASK_FILE_PATH)
        for task in task_list:
            if task["state"] == a.ACTIVE_STATE:
                result = new_result(task["name"], "Task", task["name"], icon=i.EDIT_ICON)
                results.append(result)
    else:
        argument = parser.generate_argument(a.ADD_TASK, query)
        results.append(new_result("Add task", query, argument, icon=i.ADD_ICON))
    display_alfred(results)

def display_menu(query):
    """
    Display menu for a given task
    """
    results = []

    # complete menu
    argument = parser.generate_argument(a.COMPLETE_TASK, query)
    complete_menu = new_result("Complete", "Mark task as completed", argument, icon=i.COMPLETE_ICON)
    results.append(complete_menu)

    # delete menu
    argument = parser.generate_argument(a.DELETE_TASK, query)
    delete_menu = new_result("Delete", "Delete task definitively", argument, icon=i.DELETE_ICON)
    results.append(delete_menu)

    display_alfred(results)

def display_nothing():
    """
    Display nothing
    """
    display_alfred([])

def display_alfred(result_list):
    """
    Display results in Alfred
    """
    output = {"items": result_list}
    print(json.dumps(output))

def new_result(title, subtitle, argument, valid=True, icon=None):
    """
    Generate a singe Alfred result from an input
    """
    result = {
        "type": "file",
        "title": title,
        "subtitle": subtitle,
        "arg": argument,
        "valid": valid
    }
    if icon is not None:
        result["icon"] = {"path": icon}
    return result
