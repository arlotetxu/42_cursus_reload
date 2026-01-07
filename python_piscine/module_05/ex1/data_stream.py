#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return "Str from DataStream Class"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        empty_dict = {}
        return empty_dict


class SensorStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []  # Saving all the sensor readings
        self.type: str = type
        self.s_reads: int = 0
        self.total_temp: float = 0
        self.temp_count = 0
        self.critical_alerts = 0
        self.read_processed = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_clean: List = self.filter_data(data_batch, criteria="")
            self.logs.append(data_clean)
            # self.total_temp = sum(v for log in self.logs for m, v in log if m == "temp")
            self.total_temp += sum(v for m, v in data_clean if m == "temp")
            # self.temp_count = sum(1 for log in self.logs for m, v in log if m == "temp")
            self.temp_count += sum(1 for m, v in data_clean if m == "temp")
            # self.critical_alerts += sum(1 for log in self.logs for m, v in log if m == "temp" and (v > 100 or v < 0))
            # self.critical_alerts += sum(1 for log in self.logs for m, v in log if m == "hum" and (v > 80 or v < 15))
            # self.critical_alerts += sum(1 for log in self.logs for m, v in log if m == "press" and (v > 1000 or v < 50))
            # stats: Dict[str, Union[str, int, float]] = self.get_stats()

        except TypeError:
            return "ERROR: Not valid (numeric) data found. Continue..."

        return (
            f"Stream ID: {self.stream_id}, "
            f"Type: {self.type}"
            "\nProcessing sensor batch: ["
            f"temp:{sum(v for m, v in data_clean if m == 'temp'):.1f}, "
            f"humidity:{sum(v for m, v in data_clean if m == 'hum'):.0f}, "
            f"pressure:{sum(v for m, v in data_clean if m == 'press'):.0f}]"
            f"\nSensor analysis: {sum(1 for m, v in data_clean)} readings processed, avg temp: {self.total_temp / self.temp_count}°C"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean: List[Any] = [(m, v / 1) for m, v in data_batch]
            self.read_processed = sum(1 for item in data_clean)

            # Save data with alerts in the data_alerts list to be returned if
            # criteria parameter == "alerts"
            # data_criteria: List[Any] = [(m, v) for m, v in data_clean \
            #     if m == "temp" and (v > 100 or v < 0) or \
            #     m == "hum" and (v > 80 or v < 15) or \
            #     m == "press" and (v > 1000 or v < 50)]
            if criteria == "High-priority":
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "temp" and (v > 100 or v < 0)
                )
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "hum" and (v > 80 or v < 15)
                )
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "press" and (v > 1000 or v < 50)
                )
            self.s_reads += 1

        except TypeError:
            return

        # if criteria == "alerts":
        #     return data_criteria
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        sensor_stats: Dict[str, Union[str, int, float]] = {}

        sensor_stats["av_temp"] = self.total_temp / self.temp_count
        sensor_stats["critical_alerts"] = self.critical_alerts
        sensor_stats["read_proc"] = self.read_processed
        return sensor_stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.t_reads: int = 0
        self.net_balance: int = 0
        self.total_ops: int = 0
        self.total_volume: int = 0
        self.large_trans: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_clean = self.filter_data(data_batch)
            # self.net = sum(-v if t == "sell" else v for t, v in data_batch)
            # data_clean.append(("net", self.net))
            self.logs.append(data_clean)
            self.total_ops = sum(
                1 for items in self.logs for t, v in items if t == "sell" or t == "buy"
            )
            self.net_balance = sum(
                -v if t == "sell" else v for items in self.logs for t, v in items
            )
            self.total_volume = sum(v for items in self.logs for t, v in items)
            # self.large_trans = sum(1 for items in self.logs for t, v in items if v > 100 )
            # stats = self.get_stats()

        except TypeError:
            return "ERROR: Not valid (numeric) data found. Continue..."

        return (
            f"Stream ID: {self.stream_id}, "
            f"Type: {self.type}"
            "\nProcessing transaction batch: "
            f"{[f'{t}:{v:.0f}' for t, v in data_batch]}"
            f"\nTransaction analysis: {sum(1 for t, v in data_batch)} operations, "
            f"net flow: {self.net_balance:+.0f} units"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        try:
            # Check if all the elements in the data_batch tuple list are numeric
            data_clean: List[Any] = [(m, v / 1) for m, v in data_batch]
            if criteria == "High-priority":
                self.large_trans += sum(1 for t, v in data_clean if v > 100)
            self.t_reads += 1
            # data_criteria:List[Any] = [(m, v) for m, v in data_batch if m == criteria]

        except TypeError:
            return

        # if criteria:
        #     return data_criteria
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        t_stats: Dict[str, Union[str, int, float]] = {}
        # t_stats["total_ops"] = sum(1 for items in self.logs for t, v in items if t == "sell" or t == "buy")
        # t_stats["net_balance"] = sum(-v if t == "sell" else v for items in self.logs for t, v in items)
        # t_stats["total_volume"] = sum(v for items in self.logs for t, v in items)
        t_stats["large_trans"] = self.large_trans
        t_stats["ops_proc"] = self.total_ops
        return t_stats


class EventStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.e_reads: int = 0
        self.net: int = 0
        self.error_logs = 0
        self.login_logs = 0
        self.logout_logs = 0
        self.event_proc = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_clean: List[Any] = self.filter_data(data_batch)
            self.logs.append(data_clean)

            self.event_proc += sum(1 for item in data_clean)
            # stats = self.get_stats()
        except (ValueError, TypeError):
            return "ERROR: Not valid (string) data found. Continue..."

        return (
            f"Stream ID: {self.stream_id}, Type: {self.type}"
            f"\nProcessing event batch: {data_batch}"
            f"\nEvent analysis: {sum(1 for t in data_batch)} events, "
            f"{self.error_logs} error detected"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        try:
            data_clean: List[Any] = [event + "" for event in data_batch]
            # data_criteria: List[Any] = [
            #     event for event in data_batch if event == "error"
            # ]  # TODO comprobar que hacer si criteria == "High-priority"
            self.error_logs = sum(1 for item in data_batch if item == "error")
            self.e_reads += 1

        except (TypeError, ValueError):
            return

        if criteria == "High-priority":
            self.login_logs = sum(1 for item in data_batch if item == "login")
            self.logout_logs = sum(1 for item in data_batch if item == "logout")
        # self.event_proc += sum(1 for item in data_clean)
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        e_stats: Dict[str, Union[str, int, float]] = {}
        # e_stats["error_logs"] = sum(1 for items in self.logs for item in items if item == "error")
        # e_stats["login_logs"] = sum(1 for items in self.logs for item in items if item == "login")
        # e_stats["logout_logs"] = sum(1 for items in self.logs for item in items if item == "logout")
        e_stats["error_logs"] = self.error_logs
        e_stats["event_proc"] = self.event_proc
        return e_stats


class StreamProcessor:
    def __init__(self):
        self.all_streams: List[DataStream] = []
        self.count_batch: int = 0

    def add_stream(self, stream: Any):
        if isinstance(stream, DataStream):
            self.all_streams.append(stream)

    def process_all(
        self, full_batch: List[List[Any]], criteria_in: Optional[str] = None
    ):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface..")

        self.criteria = criteria_in

        count_streams = sum(1 for stream in self.all_streams)
        count_batches = sum(1 for items in full_batch)
        limit = count_streams if count_streams < count_batches else count_batches

        i = 0
        for stream in self.all_streams:
            data = stream.filter_data(data_batch=full_batch[i], criteria=criteria_in)
            stream.process_batch(data)
            if i < limit:
                i += 1
        self.count_batch += 1

    def get_stats(self):
        # Create a dictionary with stream_id as key and the stats as value for all streams
        all_stats: Dict = {
            stream.stream_id: stream.get_stats() for stream in self.all_streams
        }
        print(f"\nBatch {self.count_batch} Results")
        print(
            f"- Sensor data: {sum(v for vals in all_stats.values() for k, v in vals.items() if k == 'read_proc')} readings processed"
        )
        print(
            f"- Transaction data: {sum(v for vals in all_stats.values() for k, v in vals.items() if k == 'ops_proc')} operations processed"
        )
        print(
            f"- Event data: {sum(v for vals in all_stats.values() for k, v in vals.items() if k == 'event_proc')} events processed"
        )

        print(f"\nStream filtering active: {self.criteria} data only")
        """
        Filtered results: 2 critical sensor alerts, 1 large transaction
        """
        critical_alerts = sum(
            v
            for id, values in all_stats.items()
            for k, v in values.items()
            if k == "critical_alerts"
        )
        large_alerts = sum(
            v
            for id, values in all_stats.items()
            for k, v in values.items()
            if k == "large_trans"
        )

        print(
            f"Filtered result: {critical_alerts} critical sensor alerts, {large_alerts} large transaction"
        )


def ft_main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()

    sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data")
    # processor.add_stream(sensor_1)
    print("\nInitializing Sensor Stream...")
    print(sensor_1.process_batch([("temp", 22.5), ("hum", 65), ("press", 1013)]))

    # sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data")
    # processor.add_stream(sensor_2)

    trans_1 = TransactionStream(stream_id="TRANS_001", type="Financial Data")
    # processor.add_stream(trans_1)
    print("\nInitializing Transaction Stream...")
    print(trans_1.process_batch([("buy", 100), ("sell", 150), ("buy", 75)]))

    # t_2 = TransactionStream(stream_id="t_002", type="Financial Data")
    # processor.add_stream(t_2)

    event_1 = EventStream(stream_id="EVENT_001", type="System Events")
    # processor.add_stream(event_1)
    print("\nInitializing Event Stream...")
    print(event_1.process_batch(["login", "error", "logout"]))

    sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data")
    processor.add_stream(sensor_2)
    trans_2 = TransactionStream(stream_id="TRANS_002", type="Financial Data")
    processor.add_stream(trans_2)
    event_2 = EventStream(stream_id="EVENT_002", type="System Events")
    processor.add_stream(event_2)

    full_batch = [
        [("temp", 101), ("press", 1924)],
        [("buy", 100), ("sell", 250), ("buy", 75), ("buy", 75)],
        ["login", "error", "login"],
    ]
    processor.process_all(full_batch, criteria_in="High-priority")
    processor.get_stats()

    print("\nAll streams processed successfully. Nexus throughput optimal.")


ft_main()
