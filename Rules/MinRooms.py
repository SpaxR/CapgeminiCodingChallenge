# check that the least number of rooms is used
import Rule


class MinRooms(Rule.Rule):

    # override, as it is impossible to be sure where people are
    # assume it is always suboptimal
    def state_optimal(self, rooms, building):
        return False

    # override
    def path_to_opt(self, rooms, building):

        result = "Optimal room distribution:"
        # put room ids and their capacity in dictionary
        room_capacities = []
        for room in rooms:
            room_capacities[room.id] = room.workplace_reservations

        num_employees = building.total_employees_in

        # sort rooms by descending capacity
        sorted_ids = sorted(room_capacities,
                            key=room_capacities.__getitem__,
                            reverse=True)

        sorted_caps = [value for (key, value)
                       in sorted(room_capacities, key=room_capacities.__getitem__,
                                 reverse=True)]
        # distribute employees to the biggest  rooms first
        i = 0
        k = 0
        while i < num_employees:
            if (num_employees - i) <= sorted_caps[k]:
                i += (num_employees - i)
                result += str((num_employees - i)) + "People in room:" + str(sorted_ids[k]) + ","
            else:
                i += sorted_caps[k]
                result += str(sorted_caps[k]) + "People in room:" + str(sorted_ids[k]) + ","

        return result
