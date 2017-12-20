"""
Custom logger for simtodo
"""

from __future__ import print_function
import sys
import config

def log(message):
    """
    Log message in alfred debugger
    Use the log_error params to log in stderr, as alfred is using stdout for his filtering
    """
    if config.DEBUG == 1:
        print(message, file=sys.stderr)
