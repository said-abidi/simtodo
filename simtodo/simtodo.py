"""
First access point of simtodo app
"""

import sys
import parser
import logger
import display
import action

# workflow bloc in alfred
BLOC = int(sys.argv[1])
logger.log("Bloc '" + str(BLOC) + "'")

# argument received
ARG = sys.argv[2]
logger.log("argument received='" + ARG + "'")

if BLOC == 1:
    # first bloc is used to display tasklist or add new task
    display.display(ARG)

if BLOC == 2:
    # second bloc is used to display task menu
    if ARG.startswith(action.ADD_TASK + action.SEPARATOR):
        # ignore if it starts with an action
        display.display_nothing()
    else:
        display.display_menu(ARG)

if BLOC == 3:
    # third bloc is used to perform action
    ACTION, QUERY = parser.parse_argument(ARG)
    logger.log("action='" + ACTION + "'")
    logger.log("query='" + QUERY + "'")
    action.PERFORM_ACTION[ACTION](QUERY)