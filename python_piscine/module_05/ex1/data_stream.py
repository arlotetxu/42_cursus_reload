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
    
    def __init__(self, stream_id):
        self.stream_id = stream_id
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass
    
    def print_all():
        for stream in DataStream.full_reads:
            print(f"Clase: {stream.__class__.__name__} / stream_id: {stream.stream_id}")


class SensorStream(DataStream):
    
    sensor_counts = 0  #TODO Hacer estos atributos de instancia
    total_temp = 0
    critic_alerts = 0

    def __init__(self, stream_id: str, type: str, id_data: List[Any]):
        super().__init__(stream_id)
        self.log = {}
        self.type = type
        self.id_data = id_data

    def process_batch(self, data_batch: List[Any]) -> str:
        
        try:
            data_clean = self.filter_data(data_batch)
            for measure, value in data_clean:
                self.log[measure] = value
            stats = self.get_stats()

        except TypeError:
            return ("ERROR: Not valid data found. Exiting...")

        return  f"Stream_id: {self.stream_id}, " \
                f"Type: {self.type}" \
                f"\nProcessing sensor batch: [temp:{self.log["temp"]}, humidity:{self.log["hum"]:.0f}, pressure:{self.log["press"]:.0f}]" \
                f"\nSensor analysis: {len(self.log)} readings processed, avg temp: {stats["av_temp"]}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        '''
        Asumimos que el primer valor es la temp, segundo hum y ultimo press y que
        todos los valores han de ser numericos para que sean validos
        
        Si el valor de temperatura es superior a 100 o menor de 0 or
        el valor de humedad es superior a 80 o menor de 15 or
        el valor de presion es superior a 1000 o menor de 50,
        lo consideramos como alertas criticas
        '''
        data_clean=[]
        try:
            data_clean = [(measure, value / 1) for measure, value in data_batch]
            SensorStream.sensor_counts += 1
            SensorStream.total_temp += sum(value for measure, value in data_batch if measure == "temp")
            SensorStream.critic_alerts += sum(1 for measure, value in data_batch if measure == "temp" and (value > 100 or value < 0))
            SensorStream.critic_alerts += sum(1 for measure, value in data_batch if measure == "hum" and (value > 80 or value < 15))
            SensorStream.critic_alerts += sum(1 for measure, value in data_batch if measure == "press" and (value > 1000 or value < 50))

        except TypeError as e:
            print(e)
            print("Not numeric data found")
            return

        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        sensor_data: Dict[str, Union[str, int, float]]= {}
        sensor_data["av_temp"] = SensorStream.total_temp / SensorStream.sensor_counts
        return sensor_data

class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
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
            DataStream.filter_data(stream, self.all_streams)
            
    def process_all(self): # TODO Hay que pasar aqui los datos que tiene que procesar cada instancia
        for stream in self.all_streams:
            print(stream.process_batch(stream.id_data))
        
        

def ft_main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()
    
    print("\nInitializing Sensor Stream...")

    sensor_1_data = [("temp", 101), ("hum", "65"), ("press",1024)]
    sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data", id_data=sensor_1_data)
    processor.add_stream(sensor_1)

    sensor_2_data = [("temp", 125), ("hum", 80), ("press", 900)]
    sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data", id_data=sensor_2_data)
    processor.add_stream(sensor_2)

    processor.process_all()
    ic(SensorStream.critic_alerts)

    print("\nTodas lecturas en DataStream: ")
    DataStream.print_all()

ft_main()