class SampleMetaData:
    sampling_start_time = 1600000000  # int64 UNIX-Timestamp
    sampling_stop_time = 1600000000  # int64 UNIX-Timestamp
    sampling_interval = 1  # int32 Time in Minutes  (1-1440)

    def __init__(self, json):
        self.sampling_start_time = json['samplingStartTime']
        self.sampling_stop_time = json['samplingStopTime']
        self.sampling_interval = json['samplingInterval']
