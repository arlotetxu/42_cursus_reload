#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from icecream import ic
'''
Authorized: class, def, super(), isinstance(), print(), try/except, list
comprehensions, from abc import ABC abstractmethod, from typing import Any
List Dict Union Optional
'''

class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return "Str from DataStream Class"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        empty_dict = {}
        return empty_dict


class SensorStream(DataStream):

    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = [] # Saving all the sensor readings
        self.type: str = type
        self.sensor_reads: int = 0
        self.total_temp: float = 0
        #self.critic_alerts = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        print("\nInitializing Sensor Stream...")
        try:
            data_clean: List = self.filter_data(data_batch, criteria="")
            self.logs.append(data_clean)
            self.total_temp = sum(v for log in self.logs for m, v in log if m == "temp")
            stats: Dict[str, Union[str, int, float]] = self.get_stats()

        except TypeError:
            return ("ERROR: Not valid (numeric) data found. Continue...")

        return  f"Stream_id: {self.stream_id}, " \
                f"Type: {self.type}" \
                "\nProcessing sensor batch: [" \
                f"temp:{sum(v for m, v in data_clean if m == "temp"):.0f}, " \
                f"humidity:{sum(v for m, v in data_clean if m == "hum"):.0f}, " \
                f"pressure:{sum(v for m, v in data_clean if m == "press"):.0f}]" \
                f"\nSensor analysis: {sum(1 for m, v in data_clean)} readings processed, avg temp: {stats["av_temp"]}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:

        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean: List[Any] = [(m, v / 1) for m, v in data_batch]

            # Save data with alerts in the data_alerts list to be returned if
            # criteria parameter == "alerts"
            data_criteria: List[Any] = [(m, v) for m, v in data_clean \
                if m == "temp" and (v > 100 or v < 0) or \
                m == "hum" and (v > 80 or v < 15) or \
                m == "press" and (v > 1000 or v < 50)]
            self.sensor_reads += 1

        except TypeError:
            return

        if criteria == "alerts":
            return data_criteria
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        sensor_stats: Dict[str, Union[str, int, float]]= {}
        critical_alerts = 0

        # self.total_temp = sum(v for log in self.logs for m, v in log if m == "temp")
        sensor_stats["av_temp"] = self.total_temp / self.sensor_reads
        critical_alerts += sum(1 for log in self.logs for m, v in log if m == "temp" and (v > 100 or v < 0))
        critical_alerts += sum(1 for log in self.logs for m, v in log if m == "hum" and (v > 80 or v < 15))
        critical_alerts += sum(1 for log in self.logs for m, v in log if m == "press" and (v > 1000 or v < 50))
        sensor_stats["critial_alerts"] = critical_alerts
        return sensor_stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.t_reads: int = 0
        self.net: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("\nInitializing taction Stream...")
        try:
            data_clean = self.filter_data(data_batch)
            # self.net = sum(-v if t == "sell" else v for t, v in data_batch)
            # data_clean.append(("net", self.net))
            self.logs.append(data_clean)
            stats = self.get_stats()

        except TypeError:
            return ("ERROR: Not valid (numeric) data found. Continue...")

        return  f"Stream_id: {self.stream_id}, " \
                f"Type: {self.type}" \
                "\nProcessing taction batch: " \
                f"{[f"{t}:{v:.0f}" for t, v in data_batch]}" \
                f"\ntaction analysis: {sum(1 for t, v in data_batch)} ops, "\
                f"net flow: {stats["net_balance"]:+.0f} units"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean:List[Any] = [(m, v / 1) for m, v in data_batch]
            self.t_reads += 1
            data_criteria:List[Any] = [(m, v) for m, v in data_batch if m == criteria]

        except TypeError:
            return

        if criteria:
            return data_criteria
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        t_stats: Dict[str, Union[str, int, float]]= {}
        t_stats["total_ops"] = sum(1 for items in self.logs for t, v in items if t == "sell" or t == "buy")
        t_stats["net_balance"] = sum(-v if t == "sell" else v for items in self.logs for t, v in items)
        t_stats["total_volume"] = sum(v for items in self.logs for t, v in items)
        return t_stats


class EventStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.events_reads: int = 0
        self.net: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("\nInitializing Event Stream...")
        try:
            data_clean: List[Any] = self.filter_data(data_batch)
            self.logs.append(data_clean)
            # stats = self.get_stats()
        except ValueError, TypeError:
            return ("ERROR: Not valid (string) data found. Continue...")

        return  f"Stream ID: {self.stream_id}, Type: {self.type}" \
                f"\nProcessing event batch: {data_batch}" \
                f"\nEvent analysis: {sum(1 for t in data_batch)} events, " \
                f"{sum(1 for t in data_batch if t == "error")} error detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        try:
            data_clean: List[Any] = [event + "" for event in data_batch]
            data_criteria: List[Any] = [event for event in data_batch if event == criteria]
            self.events_reads += 1
            
        except TypeError, ValueError:
            return

        if criteria:
            return data_criteria
        return data_clean
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamProcessor:

    def __init__(self):
        self.all_streams:List[DataStream] = []
    
    def add_stream(self, stream: Any):
        if isinstance(stream, DataStream):
            self.all_streams.append(stream)
            
    def process_all(self, full_batch: List[List[Any]], criteria_in: Optional[str]=None):
        i = 0
        for stream in self.all_streams:
            data = stream.filter_data(data_batch=full_batch[i], criteria=criteria_in)
            print(stream.process_batch(data))
            if i < len(self.all_streams):
                i += 1
        

def ft_main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()
    
    sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data")
    processor.add_stream(sensor_1)
    
    sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data")
    processor.add_stream(sensor_2)
    
    t_1 = TransactionStream(stream_id="t_001", type="Financial Data")
    processor.add_stream(t_1)
    
    t_2 = TransactionStream(stream_id="t_002", type="Financial Data")
    processor.add_stream(t_2)
    
    event_1 = EventStream(stream_id="EVENT_001", type="System Events")
    processor.add_stream(event_1)
    
    full_batch = [[("temp", 101), ("hum", 65), ("press",924)],
                  [("temp", 198), ("hum", 80), ("press", 900)],
                  [("buy", 100), ("sell", 150),],
                  [("buy", 100), ("sell", 250), ("buy", 75)],
                  ["login", "error", "logout"],
                  ]
    processor.process_all(full_batch, criteria_in="")

ft_main()