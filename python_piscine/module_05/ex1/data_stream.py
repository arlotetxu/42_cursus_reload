#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """
    Abstract base class for handling data streams.

    Attributes:
        stream_id (str): Unique identifier for the data stream.

    Methods:
        process_batch(data_batch: List[Any]) -> str:
            Abstract method to process a batch of data. Must be implemented
            by subclasses.

        filter_data(data_batch: List[Any], criteria: Optional[str] = None) ->
            List[Any]:
            Filters the provided data batch based on the given criteria.
            Returns the filtered data batch.

        get_stats() -> Dict[str, Union[str, int, float]]:
            Returns statistics about the data stream as a dictionary.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a new instance of the class with the given stream ID.

        Args:
            stream_id (str): The unique identifier for the data stream.
        """

        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data and returns a string result.

        Args:
            data_batch (List[Any]): A list containing the batch of data to be
                processed.

        Returns:
            str: A string representing the result of processing the data
                batch.
        """

        return "Str from DataStream Class"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filters a batch of data based on the provided criteria.

        Args:
            data_batch (List[Any]): The batch of data to filter.
            criteria (Optional[str], optional): The filtering criteria.
                Defaults to None.

        Returns:
            List[Any]: The filtered batch of data.
        """

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Returns a dictionary containing statistics for the data stream.

        The dictionary uses the stream ID as the key and an empty string as
            the value.
        The return type annotation indicates that the dictionary values can
            be of type str, int, or float.

        Returns:
            Dict[str, Union[str, int, float]]: A dictionary with the
                stream ID as the key and an empty string as the value.
        """

        empty_dict: Dict = {}
        empty_dict[self.stream_id] = ""
        return empty_dict


class SensorStream(DataStream):
    """
    SensorStream is a subclass of DataStream designed to process and analyze
        batches of sensor data.

    Attributes:
        logs (List): Stores all processed sensor readings.
        type (str): Type of sensor stream (e.g., temperature, humidity,
            pressure).
        s_reads (int): Number of sensor read batches processed.
        total_temp (float): Cumulative sum of temperature readings.
        temp_count (int): Number of temperature readings processed.
        critical_alerts (int): Count of critical alerts detected in sensor
            data.
        read_processed (int): Number of readings processed in the last batch.

    Methods:
        __init__(stream_id: str, type: str):
            Initializes a SensorStream instance with a stream ID and type.

        process_batch(data_batch: List[Any]) -> str:
            Processes a batch of sensor data, updates statistics, and returns
            a summary string.
            Handles invalid data types gracefully.

        filter_data(data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
            Filters and validates sensor data. If criteria is
                "High-priority", counts critical alerts.
            Returns cleaned data.

        get_stats() -> Dict[str, Union[str, int, float]]:
            Returns a dictionary of sensor statistics including average
                temperature, critical alerts, and readings processed.
    """

    def __init__(self, stream_id: str, type: str):
        """
        Initialize a data stream instance.

        Args:
            stream_id (str): Unique identifier for the data stream.
            type (str): Type of the data stream.

        Attributes:
            logs (List): Stores log entries related to the data stream.
            type (str): Type of the data stream.
            s_reads (int): Number of successful reads.
            total_temp (float): Accumulated temperature readings.
            temp_count (int): Number of temperature readings processed.
            critical_alerts (int): Number of critical alerts encountered.
            read_processed (int): Number of reads processed.
        """

        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.s_reads: int = 0
        self.total_temp: float = 0
        self.temp_count: int = 0
        self.critical_alerts: int = 0
        self.read_processed: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of sensor data, updates internal statistics, and
        returns a summary string.

        Args:
            data_batch (List[Any]): A list of sensor data readings to be
                processed.

        Returns:
            str: A formatted summary of the processed batch.

        Side Effects:
            - Updates internal logs with cleaned data.
            - Updates total temperature, temperature count, and critical
                alerts counters.

        Exceptions:
            TypeError: If non-numeric data is found in the batch, prints an
                error message and returns None.
        """

        try:
            data_clean: List[Any] = self.filter_data(data_batch)
            self.logs.append(data_clean)
            self.total_temp += sum(v for m, v in data_clean if m == "temp")
            self.temp_count += sum(1 for m, v in data_clean if m == "temp")

        except (TypeError):
            print("\nERROR: Not valid (numeric) data found in"
                  "Sensor Stream.Continue...")
            return

        return (
            f"Stream ID: {self.stream_id}, "
            f"Type: {self.type}"
            "\nProcessing sensor batch: ["
            f"temp:{sum(v for m, v in data_clean if m == 'temp'):.1f}, "
            f"humidity:{sum(v for m, v in data_clean if m == 'hum'):.0f}, "
            f"pressure:{sum(v for m, v in data_clean if m == 'press'):.0f}]"
            f"\nSensor analysis: {sum(1 for m, v in data_clean)} readings "
            f"processed, avg temp: {self.total_temp / self.temp_count}°C"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filters and processes a batch of sensor data according to specified
        criteria.

        Args:
            data_batch (List[Any]): A list of tuples, each containing a
                sensor type and its value.
            criteria (Optional[str], optional): A string specifying the
                filtering criteria. If set to "High-priority", increments
                critical alert counters for out-of-range values. Defaults to
                None.

        Returns:
            List[Any]: The cleaned data batch as a list of tuples with
                numeric values. If an exception occurs, returns None.

        Raises:
            TypeError: If the input data_batch contains non-numeric values or
                is improperly formatted.

        Side Effects:
            - Updates self.read_processed with the number of processed items.
            - Increments self.critical_alerts if "High-priority" criteria is
                met.
            - Increments self.s_reads for each call.
        """

        try:
            data_clean: List[Any] = [(m, v / 1) for m, v in data_batch]
            self.read_processed = sum(1 for item in data_clean)

            if criteria == "High-priority data only":
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "temp" and
                    (v > 100 or v < 0))
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "hum" and
                    (v > 80 or v < 15))
                self.critical_alerts += sum(
                    1 for m, v in data_clean if m == "press" and
                    (v > 1000 or v < 50))
            self.s_reads += 1

        except (TypeError):
            return

        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Calculates and returns statistics about the sensor data.

        Returns:
            Dict[str, Union[str, int, float]]: A dictionary containing:
                - "av_temp": The average temperature (float), or omitted if
                    no valid temperature readings.
                - "critical_alerts": The number of critical alerts (int).
                - "read_proc": The number of processed readings (int).

        Notes:
            If there are no numeric temperature values, "av_temp" will not
            be included in the result, and a message will be printed to
            notify the user.
        """

        sensor_stats: Dict[str, Union[str, int, float]] = {}
        try:
            sensor_stats["av_temp"] = self.total_temp / self.temp_count
        except (ZeroDivisionError):
            print("As there are not numeric values, "
                  "data cannot be processed...")
        sensor_stats["critical_alerts"] = self.critical_alerts
        sensor_stats["read_proc"] = self.read_processed
        return sensor_stats


class TransactionStream(DataStream):
    """
    A class representing a transaction data stream that extends DataStream.

    TransactionStream processes batches of financial transaction data
    (buy/sell operations), maintains logs, and tracks various statistics
    such as net balance, total volume, and large transactions.

    Attributes:
        logs (List): A list to store log entries of processed transaction
            batches.
        t_reads (int): Counter for the number of read/filter operations
            performed.
        net_balance (int): The net balance calculated from all transactions
            (buys positive, sells negative).
        total_ops (int): The total number of transaction operations
            processed.
        total_volume (int): The total absolute volume of all transactions.
        large_trans (int): Counter for transactions with values greater
            than 100.

    Methods:
        __init__(stream_id: str, type: str) -> None:
            Initializes a new TransactionStream instance.
        process_batch(data_batch: List[Any]) -> str:
            Processes a batch of transaction data and returns a summary.
        filter_data(data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
            Filters and validates transaction data based on optional criteria.
        get_stats() -> Dict[str, Union[str, int, float]]:
            Returns statistics about processed transactions.
    """

    def __init__(self, stream_id: str, type: str) -> None:
        """
        Initializes a new instance of the class with the given stream ID and
        type.

        Args:
            stream_id (str): The unique identifier for the data stream.
            type (str): The type of the data stream.

        Attributes:
            logs (List): A list to store log entries related to the stream.
            type (str): The type of the data stream.
            t_reads (int): Counter for the number of read operations.
            net_balance (int): The net balance associated with the stream.
            total_ops (int): The total number of operations performed.
            total_volume (int): The total volume processed by the stream.
            large_trans (int): Counter for large transactions.
        """

        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.t_reads: int = 0
        self.net_balance: int = 0
        self.total_ops: int = 0
        self.total_volume: int = 0
        self.large_trans: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of transaction data, updates internal logs and
        statistics, and returns a summary string.

        Args:
            data_batch (List[Any]): A list of transaction tuples, where each
            tuple contains a transaction type (e.g., "buy" or "sell") and a
            numeric value.

        Returns:
            str: A summary of the processed transaction batch, including
                stream ID, type, transaction details, number of operations,
                and net flow. Returns None if invalid (non-numeric) data is
                encountered.

        Raises:
            None explicitly, but prints an error message and returns None
            if a TypeError occurs during processing.
        """

        try:
            data_clean: List[Any] = self.filter_data(data_batch)
            self.logs.append(data_clean)
            self.total_ops = sum(1 for items in self.logs for t, v in items)
            self.net_balance = sum(
                -v if t == "sell" else v for items in self.logs
                for t, v in items
            )
            self.total_volume = sum(v for items in self.logs
                                    for t, v in items)

        except (TypeError):
            print("\nERROR: Not valid (numeric) data found "
                  "in Transaction Stream. Continue...")
            return

        return (
            f"Stream ID: {self.stream_id}, "
            f"Type: {self.type}"
            "\nProcessing transaction batch: "
            f"{[f'{t}:{v:.0f}' for t, v in data_batch]}"
            f"\nTransaction analysis: {sum(1 for t, v in data_batch)} "
            "operations, "
            f"net flow: {self.net_balance:+.0f} units"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filters and processes a batch of data tuples based on the provided
        criteria.
        Args:
            data_batch (List[Any]): A list of tuples, where each tuple
                contains a marker and a numeric value.
            criteria (Optional[str], optional): A string specifying the
                filtering criteria. If set to "High-priority", increments the
                `large_trans` attribute for each value greater than 100.
                Defaults to None.
        Returns:
            List[Any]: A cleaned list of tuples with numeric values
                processed. If an error occurs during processing, returns None.
        Raises:
            None: Any TypeError encountered during processing is caught and
                handled internally.
        """
        try:
            data_clean: List[Any] = [(m, v / 1) for m, v in data_batch]
            if criteria == "High-priority data only":
                self.large_trans += sum(1 for t, v in data_clean if v > 100)
            self.t_reads += 1

        except (TypeError):
            return

        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Returns a dictionary containing statistics about the data stream.

        Returns:
            Dict[str, Union[str, int, float]]: A dictionary with the
                following keys:
                - "large_trans": The number of large transactions.
                - "ops_proc": The total number of operations processed.
        """

        t_stats: Dict[str, Union[str, int, float]] = {}
        t_stats["large_trans"] = self.large_trans
        t_stats["ops_proc"] = self.total_ops
        return t_stats


class EventStream(DataStream):
    """
    EventStream is a subclass of DataStream designed to process and analyze
    batches of event data.

    Attributes:
        logs (List): Stores lists of cleaned event data batches.
        type (str): The type/category of the event stream.
        e_reads (int): Counter for the number of times data batches have been
            read/filtered.
        net (int): Reserved for network-related statistics (currently unused).
        error_logs (int): Number of "error" events detected in the most
            recent batch.
        login_logs (int): Number of "login" events detected (when criteria is
            "High-priority").
        logout_logs (int): Number of "logout" events detected (when criteria
            is "High-priority").
        event_proc (int): Total number of events processed.

    Methods:
        __init__(stream_id: str, type: str):
            Initializes the EventStream with a stream ID and type.

        process_batch(data_batch: List[Any]) -> str:
            Processes a batch of event data, filters it, updates statistics,
            and returns a summary string. Handles invalid data by printing
            an error message.

        filter_data(data_batch: List[Any], criteria: Optional[str] = None)
            -> List[Any]:
            Cleans and filters the input data batch. Updates error, login,
            and logout counters based on criteria. Returns the cleaned data
            batch.

        get_stats() -> Dict[str, Union[str, int, float]]:
            Returns a dictionary with statistics about processed events,
            including error logs and total events processed.
    """

    def __init__(self, stream_id: str, type: str) -> None:
        """
        Initializes a new instance of the class with the given stream ID
        and type.

        Args:
            stream_id (str): The unique identifier for the data stream.
            type (str): The type of the data stream.

        Attributes:
            logs (List): A list to store log entries.
            type (str): The type of the data stream.
            e_reads (int): Counter for read events, initialized to 0.
            net (int): data net balance (buy - sell), initialized to 0.
            error_logs (int): Counter for error logs, initialized to 0.
            login_logs (int): Counter for login logs, initialized to 0.
            logout_logs (int): Counter for logout logs, initialized to 0.
            event_proc (int): Counter for processed events, initialized to 0.
        """

        super().__init__(stream_id)
        self.logs: List = []
        self.type: str = type
        self.e_reads: int = 0
        self.net: int = 0
        self.error_logs: int = 0
        self.login_logs: int = 0
        self.logout_logs: int = 0
        self.event_proc: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data events, filters the data, updates logs and
        event counters, and returns a summary string of the processing
        results.

        Args:
            data_batch (List[Any]): A list of data items to be processed.

        Returns:
            str: A summary of the stream processing, including stream ID,
                type, number of events processed, and error count.
                Returns None if invalid data is encountered.

        Raises:
            ValueError: If invalid data is found during filtering.
            TypeError: If data types are incorrect during filtering.

        Side Effects:
            - Appends filtered data to self.logs.
            - Increments self.event_proc by the number of valid events.
            - Prints an error message if invalid data is encountered.
        """

        try:
            data_clean: List[Any] = self.filter_data(data_batch)
            self.logs.append(data_clean)

            self.event_proc += sum(1 for item in data_clean)
        except (ValueError, TypeError):
            print("\nERROR: Not valid (string) data found in Event Stream. "
                  "Continue...")
            return

        return (
            f"Stream ID: {self.stream_id}, Type: {self.type}"
            f"\nProcessing event batch: {data_batch}"
            f"\nEvent analysis: {sum(1 for t in data_batch)} events, "
            f"{self.error_logs} error detected"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filters and processes a batch of event data based on specified
        criteria.
        Args:
            data_batch (List[Any]): A list of event data to be processed.
            criteria (Optional[str], optional): A string specifying the
                filtering criteria. If set to "High-priority", additional
                login and logout event counts are updated. Defaults to None.
        Returns:
            List[Any]: A cleaned list of event data as strings.
        Side Effects:
            Updates the following instance attributes:
                - self.error_logs: Number of "error" events in data_batch.
                - self.e_reads: Increments by 1 for each call.
                - self.login_logs: Number of "login" events if criteria is
                    "High-priority".
                - self.logout_logs: Number of "logout" events if criteria is
                    "High-priority".
        Raises:
            Returns None if a TypeError or ValueError occurs during processing.
        """

        try:
            data_clean: List[Any] = [event + "" for event in data_batch]
            self.error_logs = sum(1 for item in data_batch if item == "error")
            self.e_reads += 1

        except (TypeError, ValueError):
            return

        if criteria == "High-priority data only":
            self.login_logs = sum(1 for item in data_batch if item == "login")
            self.logout_logs = sum(1 for item in data_batch
                                   if item == "logout")
        return data_clean

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Returns a dictionary containing statistics about error logs and event
        processing.
        Returns:
            Dict[str, Union[str, int, float]]:
                A dictionary with the following keys:
                    - "error_logs": The error logs associated with the data
                        stream.
                    - "event_proc": The event processing statistics.
        """

        e_stats: Dict[str, Union[str, int, float]] = {}
        e_stats["error_logs"] = self.error_logs
        e_stats["event_proc"] = self.event_proc
        return e_stats


class StreamProcessor:
    """
    StreamProcessor is a class for managing and processing multiple data
    streams polymorphically.

    Attributes:
        all_streams (List[DataStream]): List of all added data streams.
        count_batch (int): Counter for the number of processed batches.
        criteria (Optional[str]): Filtering criteria used during processing.

    Methods:
        add_stream(stream: Any):
            Adds a DataStream instance to the processor if the type matches.

        process_all(full_batch: List[List[Any]],
            criteria_in: Optional[str] = None):
            Processes all registered streams with corresponding data batches,
            applying optional filtering criteria. Each stream's filter_data
            and process_batch methods are called.

        get_stats():
            Aggregates and prints statistics from all streams, including
            processed readings, operations, events, and filtered results such
            as critical alerts and large transactions.
    """

    def __init__(self) -> None:
        """
        Initializes the DataStream object with an empty list of all streams
        and a batch counter set to zero.
        """

        self.all_streams: List[DataStream] = []
        self.count_batch: int = 0

    def add_stream(self, stream: Any) -> None:
        """
        Adds a stream to the list of all streams if it is an instance of
        DataStream.

        Args:
            stream (Any): The stream object to be added.

        Returns:
            None
        """

        if isinstance(stream, DataStream):
            self.all_streams.append(stream)

    def process_all(self, full_batch: List[List[Any]],
                    criteria_in: Optional[str] = None) -> None:
        """
        Processes all data streams in the `all_streams` attribute using the
        provided batches and optional filtering criteria.

        Args:
            full_batch (List[List[Any]]): A list of data batches, where each
                batch is a list of items to be processed by the corresponding
                stream.
            criteria_in (Optional[str], optional): An optional string
                specifying the filtering criteria to be applied to each batch
                before processing. Defaults to None.

        Returns:
            None

        Side Effects:
            - Prints information about the processing to the console.
            - Updates the `criteria` attribute with the provided criteria.
            - Increments the `count_batch` attribute after processing.
            - For each stream in `all_streams`, filters and processes the
                corresponding batch from `full_batch`.
        """

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface..")

        self.criteria: str = criteria_in

        count_streams: int = sum(1 for stream in self.all_streams)
        count_batches: int = sum(1 for items in full_batch)
        limit: int = count_streams if count_streams < count_batches \
            else count_batches

        i = 0
        for stream in self.all_streams:
            data = stream.filter_data(data_batch=full_batch[i],
                                      criteria=criteria_in)
            stream.process_batch(data)
            if i < limit:
                i += 1
        self.count_batch += 1

    def get_stats(self) -> None:
        """
        Prints a summary of statistics for all data streams in the current
        batch.

        This method aggregates and displays the number of processed sensor
        readings, transaction operations, and event data across all streams.
        It also reports the number of critical sensor alerts and large
        transactions detected after applying the current filtering criteria.

        Outputs:
            - Batch number and results summary.
            - Total sensor readings, transaction operations, and event data
                processed.
            - Active filtering criteria.
            - Number of critical sensor alerts and large transactions after
                filtering.
        """

        all_stats: Dict[str, Union[str, int, float]] = {
            stream.stream_id:
            stream.get_stats() for stream in self.all_streams
        }
        print(f"\nBatch {self.count_batch} Results")

        sensor_readings: int = sum(
            v for vals in all_stats.values()
            for k, v in vals.items()
            if k == 'read_proc'
        )
        print(f"- Sensor data: {sensor_readings} readings processed")

        trans_ops: int = sum(
            v for vals in all_stats.values()
            for k, v in vals.items()
            if k == 'ops_proc'
        )
        print(f"- Transaction data: {trans_ops} operations processed")

        event_proc: int = sum(
            v for vals in all_stats.values()
            for k, v in vals.items()
            if k == 'event_proc'
        )
        print(f"- Event data: {event_proc} events processed")

        print(f"\nStream filtering active: {self.criteria}")

        critical_alerts: int = sum(
            v
            for id, values in all_stats.items()
            for k, v in values.items()
            if k == "critical_alerts"
        )
        large_alerts: int = sum(
            v
            for id, values in all_stats.items()
            for k, v in values.items()
            if k == "large_trans"
        )

        print(
            f"Filtered results: {critical_alerts} critical sensor alerts, "
            f"{large_alerts} large transaction"
        )


def ft_main():
    """
    Main function demonstrating the Code Nexus Polymorphic Stream System.

    This function showcases the usage of different stream types
    (SensorStream, TransactionStream, EventStream) and the StreamProcessor
    for batch processing.

    The demonstration includes:
        - Individual stream initialization and batch processing for each
            stream type
        - Adding multiple streams to a centralized StreamProcessor
        - Processing all streams simultaneously with specified criteria
        - Displaying processing statistics

    Returns:
        None
    """

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()

    sensor_1 = SensorStream(stream_id="SENSOR_001", type="Environmental Data")
    print("\nInitializing Sensor Stream...")
    print(sensor_1.process_batch([("temp", 22.5), ("hum", 65),
                                  ("press", 1013)]))

    trans_1 = TransactionStream(stream_id="TRANS_001", type="Financial Data")
    print("\nInitializing Transaction Stream...")
    print(trans_1.process_batch([("buy", 100), ("sell", 150), ("buy", 75)]))

    event_1 = EventStream(stream_id="EVENT_001", type="System Events")
    print("\nInitializing Event Stream...")
    print(event_1.process_batch(["login", "error", "logout",]))

    sensor_2 = SensorStream(stream_id="SENSOR_002", type="Environmental Data")
    processor.add_stream(sensor_2)
    trans_2 = TransactionStream(stream_id="TRANS_002", type="Financial Data")
    processor.add_stream(trans_2)
    event_2 = EventStream(stream_id="EVENT_002", type="System Events")
    processor.add_stream(event_2)

    full_batch = [
        [("temp", 101), ("press", 1924),],
        [("buy", 100), ("sell", 250), ("buy", 75), ("buy", 75),],
        ["login", "error", "login", ],
    ]
    processor.process_all(full_batch, criteria_in="High-priority data only")
    processor.get_stats()

    print("\nAll streams processed successfully. Nexus throughput optimal.")


ft_main()
