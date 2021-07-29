import  Rule
import Api.RoomSensor
import Api.RoomData
import Api.BuildingData

# Do not open windows while heating or air conditioning,
# or prevent heating and air conditioning at the same time
class Windows(Rule.Rule):

    # override
    def state_optimal(self, rooms, building):

        for room in rooms:

            if (room.sensors.windows_open
                and (room.sensors.air_conditioning_running or
                     room.sensors.heater_running)) or (room.sensors.air_conditioning_running and room.sensors.heater_running):
                return False

        return True

    # override
    def path_to_opt(self, rooms, building):
        result = "Heater, aircon, windows:"
        for room in rooms:
            if room.sensors.windows_open and room.sensors.air_conditioning_running and room.sensors.heater_running:

                result += "Turn off 2 of the following in room:" + str(room.id) + "Heater, air conditioning or windows!"

            elif room.sensors.windows_open and room.sensors.heater_running:
                result += "Turn off either the heater or close the windows in room:" + str(room.id) + ",  "
            elif room.sensors.windows_open and room.sensors.air_conditioning_running:
                result += "Turn off either the air conditioning or close the windows in room:" + str(room.id) + ", "
            elif room.sensors.air_conditioning_running and room.sensors.heater_running:
                result += "Turn off either the air conditioning or the heater in room:" + str(room.id) + ", "
        if result == "Heater, aircon, windows:":
            result = "No two of the heater air conditioning or opened windows at a time! Good job!"
        return result
