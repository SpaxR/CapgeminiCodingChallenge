from Api import SampleMetaData
from Api.RoomSensor import RoomSensor


class RoomData:
    sampling_meta_data = None
    id = None  # string ([A-Z])
    power_consumption = 0  # double (kW)
    temperature = 0  # float  (°C)
    sensors = []  # Array
    workplace_reservations = 0  # Maximum parallel workplace reservations (0-4)

    def __init__(self, meta_data: SampleMetaData, json):
        self.sampling_meta_data = meta_data
        self.id = json["id"]
        self.power_consumption = json["powerConsumption"]
        self.temperature = json["temperature"]
        self.sensors = RoomSensor(json["sensors"])
        self.workplace_reservations = json["workplaceReservations"]
