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
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):

    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = [] # Saving all the sensor readings
        self.type: str = type
        self.sensor_reads: int = 0
        self.total_temp: float = 0
        #self.critic_alerts = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_clean: List = self.filter_data(data_batch)
            self.logs.append(data_clean)
            stats: Dict[str, Union[str, int, float]] = self.get_stats()

        except TypeError:
            return ("ERROR: Not valid data found. Continue...")

        return  "\nInitializing Sensor Stream..." \
                f"\nStream_id: {self.stream_id}, " \
                f"Type: {self.type}" \
                "\nProcessing sensor batch: [" \
                f"temp:{sum(value for measure, value in data_clean if measure == "temp"):.0f}, " \
                f"humidity:{sum(value for measure, value in data_clean if measure == "hum"):.0f}, " \
                f"pressure:{sum(value for measure, value in data_clean if measure == "press"):.0f}]" \
                f"\nSensor analysis: {len(data_batch)} readings processed, avg temp: {stats["av_temp"]}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        '''
        Asumimos que el primer valor es la temp, segundo hum y ultimo press y que
        todos los valores han de ser numericos para que sean validos
        
        Si el valor de temperatura es superior a 100 o menor de 0 or
        el valor de humedad es superior a 80 o menor de 15 or
        el valor de presion es superior a 1000 o menor de 50,
        lo consideramos como alertas criticas
        '''
        data_clean: List = []
        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean = [(measure, value / 1) for measure, value in data_batch]
            self.sensor_reads += 1

        except TypeError as e:
            print(e)
            print("Not numeric data found")
            return

        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        sensor_stats: Dict[str, Union[str, int, float]]= {}
        critical_alerts = 0
        
        self.total_temp = sum(value for log in self.logs for measure, value in log if measure == "temp")
        sensor_stats["av_temp"] = self.total_temp / self.sensor_reads
        
        critical_alerts += sum(1 for log in self.logs for measure, value in log if measure == "temp" and (value > 100 or value < 0))
        critical_alerts += sum(1 for log in self.logs for measure, value in log if measure == "hum" and (value > 80 or value < 15))
        critical_alerts += sum(1 for log in self.logs for measure, value in log if measure == "press" and (value > 1000 or value < 50))
        sensor_stats["critial_alerts"] = critical_alerts
        return sensor_stats

class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.sensor_reads: int = 0
        self.net: int = 0
        
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_clean = self.filter_data(data_batch)
            self.net = sum(-value if trans == "sell" else value for trans, value in data_batch)
            data_clean.append(("net", self.net))
            self.logs.append(data_clean)
            to_print: List[str] = [f"{trans}:{value}" for trans, value in data_batch]
            #stats = self.get_stats()

        except TypeError:
            return ("ERROR: Not valid data found. Continue...")

        return  "\nInitializing Transaction Stream..." \
                f"\nStream_id: {self.stream_id}, " \
                f"Type: {self.type}" \
                "\nProcessing transaction batch: " \
                f"{to_print}" \
                f"\nTransaction analysis: {len(data_batch)} operations, "\
                f"net flow: {self.net:+} units"
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        data_clean=[]
        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean = [(measure, value / 1) for measure, value in data_batch]
            self.sensor_reads += 1

        except TypeError as e:
            print(e)
            print("Not numeric data found")
            return

        return data_clean
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        # TODO --> Que información saca aqui este metodo???
        pass

class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamProcessor:

    def __init__(self):
        self.all_streams:List[DataStream] = []
    
    def add_stream(self, stream: Any):
        if isinstance(stream, DataStream):
            self.all_streams.append(stream)
            
    def process_all(self, full_batch: List[List[Any]]):
        i = 0
        for stream in self.all_streams:
            print(stream.process_batch(full_batch[i]))
            i += 1
        

def ft_main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()

    # sensor_1_data = [("temp", 101), ("hum", 65), ("press",1024)]
    # sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data", id_data=sensor_1_data)
    sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data")
    processor.add_stream(sensor_1)
    sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data")
    processor.add_stream(sensor_2)
    trans_1 = TransactionStream(stream_id="TRANS_001", type="Financial Data")
    processor.add_stream(trans_1)

    # sensor_2_data = [("temp", 125), ("hum", 80), ("press", 900)]
    # sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data", id_data=sensor_2_data)
    # processor.add_stream(sensor_2)
    
    full_batch = [[("temp", 101), ("hum", 65), ("press",1024)],
                  [("temp", 125), ("hum", 80), ("press", 900)],
                  [("buy", 100), ("sell", 150), ("buy", 75)],
                  ]
    processor.process_all(full_batch)
   #print(sensor_1.process_batch([("temp", 200), ("hum", 60), ("press",1000)]))
    
    # ic(sensor_1.critic_alerts)

ft_main()