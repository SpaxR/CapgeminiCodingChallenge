import Rule


# check that the least number of rooms is used
class MinRooms(Rule):

    # override, as it is impossible to be sure where people are
    # assume it is always suboptimal
    def state_optimal(self, rooms, building):
        return False



    # override
    def path_to_opt(self, rooms, building):
        result = "Optimal room distribution:"
        # put roomids and their capacity in dictionary
        roomCapacities = []
        for room in rooms:
            roomCapacities[room.id]= room.workplaceReservations

        num_employees = building.totalEmployeesIn

        # sort rooms by descending capacity
        sorted_ids = sorted(roomCapacities,
                            key=roomCapacities.__getitem__,
                            reverse=True)

        sorted_caps = [value for (key, value)
                       in sorted(roomCapacities.__getitem__,
                                 reverse=True)]
        # distribute employees to the biggest  rooms first
        i = 0
        k = 0
        while(i < num_employees):
            if (num_employees- i) <= sorted_caps[k]
                i += (num_employees- i):
                result += (num_employees- i) + "People in room:" + sorted_ids[k] + ","
            else:
                i += sorted_caps[k]
                result += sorted_caps[k] + "People in room:" + sorted_ids[k] + ","


        return result


