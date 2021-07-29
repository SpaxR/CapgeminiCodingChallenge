import Rule
from Api.ApiAccess import ApiAccess


# Do not open windows more than 20 min in 2 hours
class OpenWindowsNecessary(Rule.Rule):
    # how often should measurements be taken in minutes
    freq = 5

    # for how long in the past should be looked in minutes
    interval = 120

    # how many minutes per interval are allowed
    cap = 20

    # calculates how long the window was opened for at max
    # for a room based on list of the rooms past data
    # in minutes
    def length_of_windows_opened(self, data_room):

        i = 0
        for data in data_room:
            if data.sensors.windows_opened:
                i += 1

        return i * self.freq

    # override
    def state_optimal(self, rooms, building):

        # find rooms with currently opened windows and
        # then get their last two hours of data in 5min intervals
        for room in rooms:
            if room.sensors.windows_open:
                # gets data for the room in ???
                data_room = ApiAccess.request_specific_room_data(room.id, ApiAccess.server_time - self.interval,
                                                                 ApiAccess.server_time, self.freq)

                if self.length_of_windows_opened(data_room) > self.cap:
                    return False

        return True

    # override
    def path_to_opt(self, rooms, building):

        result = ""
        # find rooms with currently opened windows and
        # then get their last two hours of data in 5min intervals
        for room in rooms:
            if room.sensors.windows_open:
                # gets data for the room of the last two hours in 5min intervals
                data_room = ApiAccess.request_specific_room_data(room.id, ApiAccess.server_time - self.interval,
                                                                 ApiAccess.server_time, self.freq)

                if self.length_of_windows_opened(data_room) > 20:
                    result += "Close the windows in room: " + str(room.id) + "     "

        return result
