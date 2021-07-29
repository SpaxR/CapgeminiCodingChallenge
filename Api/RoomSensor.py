class RoomSensor:
    light_on = False  # boolean
    windows_open = False  # boolean (True, if at least one Window open)
    roller_blinds_closed = True  # boolean (True, if more than half way closed)
    air_conditioning_running = False  # boolean
    heater_running = False  # boolean

    def __init__(self, json):
        self.light_on = json["lightOn"]
        self.windows_open = json["windowsOpen"]
        self.roller_blinds_closed = json["rollerBlindsClosed"]
        self.air_conditioning_running = json["airConditioningRunning"]
        self.heater_running = json["heaterRunning"]
