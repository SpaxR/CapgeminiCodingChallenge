from Api import SampleMetaData, BuildingData, RoomData


class LiveData:
    sampling_meta_data: SampleMetaData = None
    building_data: BuildingData = None
    rooms = []

    def __init__(self, meta_data: SampleMetaData, building_data: BuildingData, rooms_data: RoomData):
        self.sampling_meta_data = meta_data
        self.building_data = building_data
        self.rooms = rooms_data
