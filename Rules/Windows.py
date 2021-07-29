import  Rule

# Do not open windows while heating or air conditioning,
# or prevent heating and airconditioning at the same time
class Windows(Rule):

    # override
    def state_optimal(self, rooms, building):

        for room in rooms:

            if room.sensors.windowsOpen
                and (room.sensors.airConditioningRunning or
                room.sensors.heaterRunning):
                return False

        return True

    # override
    def path_to_opt(self, rooms, building):
        result = ""
        for room in rooms:
            if room.sensors.windowsOpen
                and room.sensors.airConditioningRunning and
                room.sensors.heaterRunning:

                result += "Turn off 2 of the following in room:"
                + room.id + "Heater, airconditioning or windows!"

            elif room.sensors.widowsOpen and room.sensors.heaterRunning:
                result += "Turn off either the heater or close the windows in room:" + room.id
            elif room.sensors.widowsOpen and room.sensors.airConditioningRunning:
                result += "Turn off either the air conditioning or close the windows in room:" + room.id
            elif room.sensors.airConditioningRunning and
                room.sensors.heaterRunning:
                result += "Turn off either the air conditioning or the heater in room:" + room.id

        return result