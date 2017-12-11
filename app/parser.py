"""
Parse argument used to communicate between Alfred blocs and generate them
"""

import action as a

def parse_argument(argument):
    """
    Parse the argument received by alfred module and return an action and a query
    """
    separator_index = argument.find(a.SEPARATOR)
    if separator_index:
        action = argument[:separator_index]
        query = argument[separator_index + len(a.SEPARATOR):]
        return (action, query)
    return (None, query)

def generate_argument(action, query):
    """
    Generate argument that will be transmit to other Alfred blocs
    """
    return action + a.SEPARATOR + query
