import time

import requests
from requests import Response

from Api.BuildingData import BuildingData
from Api.LiveData import LiveData
from Api.RoomData import RoomData
from Api.SampleMetaData import SampleMetaData


class ApiAccess:
    api_url = "https://rvj6rnbpxj.execute-api.eu-central-1.amazonaws.com/prod/"

    @staticmethod
    def request_live_data(interval=1):
        response = requests.get(ApiAccess.api_url + "live-data", params={'interval': interval})
        ApiAccess.__ensure_success_status(response)
        json = response.json()
        sample_data = SampleMetaData(json)
        building_data = BuildingData(sample_data, json["building"])
        rooms = []
        for room in json["rooms"]:
            rooms.append(RoomData(sample_data, room))
        return LiveData(sample_data, building_data, rooms)

    @staticmethod
    def request_building_data(begin_timestamp, end_timestamp, interval):
        ApiAccess.__ensure_timestamps_valid(begin_timestamp, end_timestamp, interval)
        response = requests.get(ApiAccess.api_url + "building", params={
            'begin-timestamp': begin_timestamp,
            'end-timestamp': end_timestamp,
            'interval': interval
        })
        ApiAccess.__ensure_success_status(response)
        json = response.json()
        results = []
        for dataset in json:
            sample_data = SampleMetaData(json)
            results.append(BuildingData(sample_data, dataset))
        return results

    @staticmethod
    def request_rooms_data(self, begin_timestamp, end_timestamp, interval):
        self.__ensure_timestamps_valid(begin_timestamp, end_timestamp, interval)
        response = requests.get(self.api_url + "room", params={
            'begin-timestamp': begin_timestamp,
            'end-timestamp': end_timestamp,
            'interval': interval
        })
        self.__ensure_success_status(response)
        json = response.json()
        results = []
        for dataset in json:
            sample_data = SampleMetaData(json)
            rooms = []
            for room in dataset["rooms"]:
                rooms.append(RoomData(sample_data, room))
            results.append(rooms)
        return results

    @staticmethod
    def request_specific_room_data(room_id, begin_timestamp, end_timestamp, interval):
        # Note: definitely not the best approach, but time is short
        data = ApiAccess.request_rooms_data(begin_timestamp, end_timestamp, interval)
        result = []
        for dataset in data:
            for room in dataset:
                if room.id is room_id:
                    result.append(room)
        return result

    @staticmethod
    def __ensure_success_status(response: Response):
        if response.status_code is not 200:
            raise Exception("Failed to call API")

    @staticmethod
    def __ensure_timestamps_valid(begin, end, interval):
        # 1 Interval = 60 seconds
        if end <= begin:
            raise ValueError('End-Timestamp is before Begin-Timestamp')
        if (end - begin) / 60 < interval:
            raise ValueError('Time between timestamp is shorter than Interval')

        pass
