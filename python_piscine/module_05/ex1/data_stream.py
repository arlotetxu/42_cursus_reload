#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
'''
Authorized: class, def, super(), isinstance(), print(), try/except, list
comprehensions, from abc import ABC abstractmethod, from typing import Any
List Dict Union Optional


$> python3 data_stream.py
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...

Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction

All streams processed successfully. Nexus throughput optimal.
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


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

class EventStream(DataStream):
    def __init__(self, id):
        self.id = id
        
    def process_batch(self, data_batch: List[Any]) -> str:
        pass


class StreamProcessor:
    streams = [] # Lista con cada instancia creada de cada stream especifico
    
    def add_stream(stream: Any):
        if isinstance(stream, DataStream):
            StreamProcessor.streams.append(stream)
        
    def print_streams():
        for stream in StreamProcessor.streams:
            print(f"Clase: {stream.__class__.__name__} / stream_id: {stream.stream_id}")


sensor_1 = SensorStream("SENSOR_001")
StreamProcessor.add_stream(sensor_1)

sensor_2 = TransactionStream("TRANS_001")
StreamProcessor.add_stream(sensor_2)

StreamProcessor.print_streams()