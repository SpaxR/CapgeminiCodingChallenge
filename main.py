import os
import time

from Api.ApiAccess import ApiAccess
# from Rules.OpenWindowsNecessary import OpenWindowsNecessary
from Rules.MinRooms import MinRooms
from Rules.Windows import Windows


def output_to_console(lines):
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')
    for line in lines:
        print(line)
    pass


ruleset = [
    MinRooms(),
    Windows(),
    # OpenWindowsNecessary()
]

while True:
    suggested_optimizations = []

    # Load Data
    data = ApiAccess.request_live_data(1)

    # Execute all Rules
    for rule in ruleset:
        if not rule.state_optimal(data.rooms, data.building_data):
            suggested_optimizations.append(rule.path_to_opt(data.rooms, data.building_data))

    # Output Data
    output_to_console(suggested_optimizations)
    f = open("suggestions.txt", "w")
    f.writelines(suggested_optimizations)
    f.close()
    time.sleep(5) # Refresh every 5 seconds
    pass

