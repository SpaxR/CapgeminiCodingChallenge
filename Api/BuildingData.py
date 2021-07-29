from Api import SampleMetaData


class BuildingData:
    sample_meta_data = None
    total_power_consumption = 0  # double (kW)
    power_consumption_data_center = 0  # double (kW)
    solar_power_output = 0  # double (kW)
    outdoor_temperature = 0  # float  (°C)
    water_consumption = 0  # float  (l)
    total_employees_in = 0  # int32

    def __init__(self, meta_data: SampleMetaData, json):
        self.sample_meta_data = meta_data
        self.total_power_consumption = json["totalPowerConsumption"]
        self.power_consumption_data_center = json["powerConsumptionDataCenter"]
        self.solar_power_output = json["solarPowerOutput"]
        self.outdoor_temperature = json["outdoorTemperature"]
        self.water_consumption = json["waterConsumption"]
        self.total_employees_in = json["totalEmployeesIn"]
        pass
