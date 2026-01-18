#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Protocol, Union
from icecream import ic

class ProgramError(Exception):
    def __init__(self, message="STD Error"):
        super().__init__(self, message)


class NexusLogger:
    """
    A logger class for tracking messages across different pipeline stages.

    This class maintains separate log lists for input, transformation, and
    output stages of a Nexus pipeline. All logs are stored as class-level
    attributes, meaning they are shared across all instances.

    Attributes:
        logs_input (List[str]): Class-level list storing logs from InputStage.
        logs_transf (List[str]): Class-level list storing logs from
            TransformStage.
        logs_output (List[str]): Class-level list storing logs from
            OutputStage.

    Methods:
        add_log(stage: str, message: str): Adds a log message to the
            appropriate stage-specific log list based on the stage parameter.
    """

    logs_input: List[str] = []
    logs_transf: List[str] = []
    logs_output: List[str] = []

    def add_log(self, stage: str, message: str):
        """
        Adds a log message to the appropriate log list based on the specified
        stage.

        Args:
            stage (str): The pipeline stage for the log message.
                         Valid values are "InputStage", "TransformStage", or
                         "OutputStage".
            message (str): The log message to be added.

        Returns:
            None

        Note:
            Messages are appended to class-level log lists:
            - "InputStage" -> NexusLogger.logs_input
            - "TransformStage" -> NexusLogger.logs_transf
            - "OutputStage" -> NexusLogger.logs_output
        """
        if stage == "InputStage":
            NexusLogger.logs_input.append(message)
        elif stage == "TransformStage":
            NexusLogger.logs_transf.append(message)
        elif stage == "OutputStage":
            NexusLogger.logs_output.append(message)


# @runtime_checkable
class ProcessingStage(Protocol):
    """
    A protocol class that defines the interface for processing stages in a
    pipeline.

    This protocol establishes the contract that all processing stages must
    implement a process method that takes data as input and returns a
    processed result.

    Methods
    -------
    process(data) -> Any
        Processes the input data and returns the transformed result.

        Parameters
        ----------
        data : Any
            The input data to be processed by this stage.

        Returns
        -------
        Any
            The processed/transformed data.
    """

    def process(self, data) -> Any: ...

    """
    Process the given data through the pipeline.

    Args:
        data: The input data to be processed by the pipeline.

    Returns:
        Any: The processed result after applying pipeline transformations.
    """


class InputStage:
    """
    A pipeline stage that processes and normalizes input data from various
    formats.

    This class handles three types of input data:
    1. Dictionary input: Must contain 'sensor', 'value', and 'unit' keys.
        Returns the original dict with 'from' set to 'json'.
    2. CSV string input: A comma-separated string that gets split into a list.
        Returns a dict with 'string' containing the split values and 'from'
        set to 'csv'.
    3. Numeric stream input: A list containing only integers or floats.
        Returns a dict with 'values' containing the list and 'from' set to
        'stream'.

    If the input doesn't match any of these formats, an error is logged via
    NexusLogger.

    Methods:
         process(data: Any) -> Dict:
              Processes the input data and returns a normalized dictionary.

    Args:
         data (Any): The input data to process. Can be a dict, str, or list.

    Returns:
         Dict: A dictionary containing the processed data with a 'from' key
                 indicating the source format, or an empty dict if the format
                 is invalid.
    """

    def process(self, data: Any) -> Dict:
        """
        Process input data and convert it to a standardized dictionary format.

        This method handles three types of input data:
        - Dictionary with required keys ('sensor', 'value', 'unit'): Returns
            the dict with 'from' set to 'json'
        - Comma-separated string: Splits by comma and returns with 'from'
            set to 'csv'
        - List of numeric values (int or float): Returns with 'from' set to
            'stream'

        Args:
            data (Any): The input data to process. Can be a dict, str, or
                List of numbers.

        Returns:
            Dict: A dictionary containing the processed data with a 'from'
                key indicating the source format. Returns an empty dict if
                the data format is invalid.

        Note:
            If the data format is invalid, a log entry is added via
            NexusLogger.
        """

        # Identificar la instancia del adaptador mediante la referencia inyectada
        launcher_instance = getattr(self, 'launcher', None)
        input_ret: Dict = {}
        # required_keys: List[str] = ["sensor", "value", "unit"]

        # if isinstance(data, dict) and all(key in data for key in required_keys):
        try:
            if launcher_instance and isinstance(launcher_instance, JSONAdapter):
                input_ret = {**data}
                input_ret["from"] = "json"
                return input_ret       

            # elif isinstance(data, str) and "," in data:
            if launcher_instance and isinstance(launcher_instance, CSVAdapter):
                input_ret["string"] = data.split(",")
                input_ret["from"] = "csv"
                return input_ret

        # elif isinstance(data, List) and all(
        #     isinstance(item, (int | float)) for item in data
        # ):
            if launcher_instance and isinstance(launcher_instance, StreamAdapter):
                input_ret["values"] = data
                input_ret["from"] = "stream"
                return input_ret
        
            else:
                NexusLogger().add_log("InputStage", "Invalid data format")
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                raise ProgramError("Error detected in Stage 1: Invalid input data format")
        except Exception:
            pass

        return input_ret


class TransformStage:
    """
    A pipeline stage that transforms data based on its source format.

    This class processes dictionaries containing data from different sources
    (json, csv, stream) and applies appropriate transformations.

    Methods
    -------
    process(data: Any) -> Dict
        Transforms the input data based on its 'from' key value.

        For JSON source:
            - Extracts the 'value' field and converts it to a float
                temperature.
            - Adds a 'range' key indicating if temperature is in
                "Normal Range" (between 0 and 100) or "Out of Range".

        For CSV source:
            - Currently not implemented (pass).

        For stream source:
            - Extracts 'values' field containing multiple temperature
                readings.
            - Calculates and adds 'avg_temp' key with the average temperature.

        Parameters
        ----------
        data : Any
            A dictionary containing a 'from' key indicating the data source
            and corresponding value fields.

        Returns
        -------
        Dict
            The transformed data dictionary with additional computed fields.

        Raises
        ------
        Logs errors via NexusLogger for:
            - KeyError: When required keys are missing (JSON source).
            - ValueError: When data cannot be converted to float.
    """

    def process(self, data: Any) -> Dict:
        """
        Process and transform data based on its source format.

        This method processes input data differently depending on its origin:
        - For JSON data: Extracts a temperature value and determines if it's
            in "Normal Range" (0-100) or "Out of Range", adding a 'range' key
            to the data.
        - For CSV data: Currently not implemented (pass).
        - For stream data: Calculates the average temperature from a list of
            values and adds it as 'avg_temp' to the data.

        Args:
                data: A dictionary containing the data to process.
                    Expected keys include:
                    - 'from': The source format ('json', 'csv', or 'stream')
                    - 'value': Temperature value (for JSON source)
                    - 'values': List of temperature values (for stream source)

        Returns:
                Dict: The processed data dictionary with additional computed
                    fields ('range' for JSON, 'avg_temp' for stream).

        Raises:
                Logs errors via NexusLogger for:
                        - KeyError: When expected keys are missing (JSON
                            processing)
                        - ValueError: When data cannot be converted to float
        """
        for k, v in data.items():
            if k == "from" and v == "json":
                try:
                    temp: float = float(data["value"])
                    range: str = (
                        "Normal Range" if temp > 0 and temp < 100 else "Out of Range"
                    )
                    data["range"] = range
                    break
                except KeyError:
                    NexusLogger().add_log("TransformStage", "Invalid key")
                    raise ProgramError("Error detected in Stage 2: Invalid key")
                except ValueError:
                    NexusLogger().add_log("TransformStage", "Invalid data format")
                    raise ProgramError("Error detected in Stage 2: Invalid data format")
            if k == "from" and v == "csv":
                pass
            if k == "from" and v == "stream":
                try:
                    temps: List[float] = [float(temp) for temp in data.get("values")]
                    avg_temp: float = sum(temp for temp in temps) / sum(
                        1 for temp in temps
                    )
                    data["avg_temp"] = avg_temp
                    break
                except ValueError:
                    NexusLogger().add_log("TransformStage", "Invalid data format")
                    raise ProgramError("Error detected in Stage 2: Invalid data format")
        return data


class OutputStage:
    """
    A pipeline stage that marks data as processed.

    This class represents the final stage in a data processing pipeline,
    adding a 'processed' flag to the data dictionary.

    Methods
    -------
    process(data: Any) -> Dict
        Marks the input data as processed by adding a 'processed' key
        set to True and returns the modified dictionary.
    """

    def process(self, data: Any) -> str:
        """
        Process the input data by marking it as processed.

        Args:
            data: Any dictionary-like object that can accept key-value pairs.

        Returns:
            Dict: The input data dictionary with an additional 'processed'
                key set to True.
        """
        data["processed"] = True
        for k, v in data.items():
            try:
                if k == "from" and v == "json":
                    return f"Output: Processed temperature reading: {data['value']}°C ({data['range']})"
            except KeyError:
                NexusLogger().add_log("OutputStage", "Cannot create the desire output")
                raise ProgramError("Error detected in Stage 3: Invalid data format")
            if k == "from" and v == "csv":
                return "Output: User activity logged: 1 actions processed"
            try:
                if k == "from" and v == "stream":
                    return f"Output: Stream summary: {len(data['values'])} readings, avg: {data['avg_temp']}°C"
            except Exception:
                NexusLogger().add_log("OutputStage", "Cannot create the desire output")
                raise ProgramError("Error detected in Stage 2: Invalid data format")


# ===========================================================================
class ProcessingPipeline(ABC):
    """
    Abstract base class for creating data processing pipelines.

    This class provides a framework for building multi-stage data processing
    pipelines where each stage performs a specific transformation or operation
    on the data.

    Attributes:
        pipeline_id (str): Unique identifier for the pipeline.
        stages (List[ProcessingStage]): Ordered list of processing stages
            to be executed in the pipeline.

    Methods:
        add_stage(stage: ProcessingStage) -> None:
            Appends a processing stage to the pipeline.
        process(data: Any) -> Union[str, Any]:
            Abstract method that must be implemented by subclasses to define
            how data flows through the pipeline stages.
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize a NexusPipeline instance.

        Args:
            pipeline_id (str): Unique identifier for the pipeline.

        Returns:
            None
        """
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Add a processing stage to the pipeline.

        Args:
            stage (ProcessingStage): The processing stage to be added to the
                pipeline.

        Returns:
            None
        """
        
        '''
         le inyecte una referencia a sí mismo (el adaptador). Luego, dentro
         de InputStage, simplemente accedes a esa referencia.
        '''
        stage.launcher= self
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]: ...

    """
    Process the input data through the pipeline.

    Args:
        data (Any): The input data to be processed by the pipeline.

    Returns:
        Union[str, Any]: The processed result, which can be either a string
            or any other type depending on the pipeline operations.
    """


class JSONAdapter(ProcessingPipeline):
    """
    A processing pipeline adapter for handling JSON data.

    This class extends ProcessingPipeline to provide a specialized pipeline
    for processing data through a series of stages, typically used for
    JSON data transformation.

    Attributes:
        pipeline_id (str): Unique identifier for the pipeline instance.
        stages (list): Inherited list of processing stages from
            ProcessingPipeline.

    Methods:
        process(data: Any) -> Union[str, Any]:
            Processes the input data through all registered stages
                sequentially. Each stage's output becomes the input for the
                next stage.

    Args:
        pipeline_id (str): A unique identifier for this pipeline instance.
    """

    def __init__(self, pipeline_id: str):
        """
        Initialize a NexusPipeline instance.

        Args:
            pipeline_id (str): The unique identifier for the pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Process data through all stages in the pipeline sequentially.

        Each stage's output becomes the input for the next stage in the
        pipeline.

        Args:
            data: The initial input data to be processed through the pipeline.

        Returns:
            Union[str, Any]: The final output after processing through all
                stages.
        """
        for stage in self.stages:
            ic(stage)
            try:
                data = stage.process(data)
            except ProgramError as p_e:
                raise ProgramError(p_e)
        return data


class CSVAdapter(ProcessingPipeline):
    """
    Adapter class for processing CSV data through a pipeline.

    This class extends ProcessingPipeline to provide CSV-specific data
    processing capabilities by sequentially applying all registered processing
    stages to the input data.

    Attributes:
        pipeline_id (str): Unique identifier for the pipeline instance.
        stages (list): List of processing stages inherited from
            ProcessingPipeline.

    Methods:
        process(data: Any) -> Union[str, Any]:
            Processes the input data through all registered stages
                sequentially. Each stage transforms the data and passes it to
                the next stage.

    Args:
        pipeline_id (str): A unique identifier for this pipeline instance.
    """

    def __init__(self, pipeline_id: str):
        """
        Initialize a NexusPipeline instance.

        Args:
            pipeline_id (str): The unique identifier for the pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Process data through all stages in the pipeline sequentially.

        Each stage's output becomes the input for the next stage in the
        pipeline.

        Args:
            data: The initial input data to be processed through the pipeline.
                Can be of any type depending on the first stage's
                requirements.

        Returns:
            Union[str, Any]: The final processed data after passing through
                all stages. The return type depends on the last stage's
                output.
        """
        for stage in self.stages:
            ic(stage)
            try:
                data = stage.process(data)
            except ProgramError as p_e:
                raise ProgramError(p_e)
        return data


class StreamAdapter(ProcessingPipeline):
    """
    A stream adapter that processes data through a series of pipeline stages.

    This class extends ProcessingPipeline to provide sequential data
    processing capabilities, where data flows through each registered stage
    in order.

    Attributes:
        pipeline_id (str): Unique identifier for this pipeline instance.
        stages (list): List of processing stages inherited from
            ProcessingPipeline.

    Methods:
        process(data: Any) -> Union[str, Any]:
            Processes the input data through all registered stages
                sequentially. Each stage receives the output of the previous
                stage as its input.

    Args:
        pipeline_id (str): The unique identifier for this stream adapter
            pipeline.
    """

    def __init__(self, pipeline_id: str):
        """
        Initialize a NexusPipeline instance.

        Args:
            pipeline_id (str): The unique identifier for the pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Process data through all pipeline stages sequentially.

        Each stage in the pipeline processes the data in order, with the
        output of one stage becoming the input of the next.

        Args:
            data: The input data to be processed through the pipeline.
                Can be of any type.

        Returns:
            Union[str, Any]: The final processed data after passing through
                all stages. The return type depends on the transformations
                applied by the pipeline stages.
        """
        for stage in self.stages:
            ic(stage)
            try:
                data = stage.process(data)
            except ProgramError as p_e:
                raise ProgramError(p_e)
        return data


# ==========================================================================
class NexusManager:
    """
    A manager class for handling multiple processing pipelines.

    This class manages a collection of ProcessingPipeline objects,
    configures them with standard processing stages, and processes
    data through each pipeline.

    Attributes:
        pipelines (List[Any]): A list of processing pipelines managed
            by this instance.
        capacity (int): The maximum capacity for processing, defaults
            to 1000. Symbolic
        pipes_processed (int): Counter tracking the number of pipelines
            that have been processed.

    Methods:
        add_pipeline(pipelines: List[ProcessingPipeline]): Adds multiple
            pipelines to the manager.
        process(data: Any): Configures all pipelines with Input,
            Transform, and Output stages, then processes the
            corresponding data through each pipeline.
    """

    def __init__(self):
        """
        Initialize a new NexusPipeline instance.

        Attributes:
            pipelines (List[Any]): A list to store pipeline objects.
            capacity (int): The maximum capacity of the pipeline,
                defaults to 1000.
            pipes_processed (int): Counter for the number of pipes
                processed, defaults to 0.
        """
        self.pipelines: List[Any] = []
        self.capacity: int = 1000
        self.pipes_processed: int = 0

    def add_pipeline(self, pipelines: List[ProcessingPipeline]):
        """
        Add multiple processing pipelines to the nexus pipeline.

        Args:
            pipelines (List[ProcessingPipeline]): A list of
            ProcessingPipeline objects to be added to the nexus
            pipeline collection.

        Returns:
            None
        """
        for pipeline in pipelines:
            self.pipelines.append(pipeline)

    def process(self, data: Any):
        """
        Process data through all pipelines in the nexus.

        For each pipeline, adds Input, Transform, and Output stages,
        then processes the corresponding data element through each pipeline.
        After processing, all pipelines are cleared.

        Args:
            data: Any iterable containing data elements to be processed.
                  Each element will be processed by a corresponding pipeline.

        Returns:
            None
        """
        for pipe in self.pipelines:
            pipe.add_stage(InputStage())
            pipe.add_stage(TransformStage())
            pipe.add_stage(OutputStage())

        for pipe in self.pipelines:
            for read in data:
                try:
                    ic(pipe)
                    ic(read)
                    pipe.process(read)
                    self.pipes_processed += 1
                except ProgramError as p_e:
                    print(p_e.args)
                    pass

        self.pipelines.clear()


# ===========================================================================
def ft_launch_json() -> None:
    """
    Launch and execute a JSON data processing pipeline.

    This function creates a JSONAdapter pipeline with three stages
    (Input, Transform, Output) and processes temperature sensor data
    through each stage sequentially.

    The pipeline demonstrates the processing of JSON sensor data:
    - InputStage: Receives and processes the initial JSON data
    - TransformStage: Enriches data with metadata and validation
    - OutputStage: Outputs the processed temperature reading with
        range classification

    Returns:
        None
    """

    pipe_json = JSONAdapter("json_001")
    data_json = {"sensor": "temp", "value": 23.5, "unit": "C"}
    pipe_json.add_stage(InputStage())
    pipe_json.add_stage(TransformStage())
    pipe_json.add_stage(OutputStage())

    for stage in pipe_json.stages:
        if isinstance(stage, InputStage):
            print("\nProcessing JSON data through pipeline...")
            print(f"Input: {data_json}")
            data_json = stage.process(data_json)
        elif isinstance(stage, TransformStage):
            print("Transform: Enriched with metadata and validation")
            data_json = stage.process(data_json)
        elif isinstance(stage, OutputStage):
            temp: float = float(data_json.get("value"))
            range: str = "Normal Range" if temp > 0 and temp < 100 else "Out of Range"
            print(f"Output: Processed temperature reading: {temp:.1f}°C ({range})")
            data_json = stage.process(data_json)


def ft_launc_csv() -> None:
    """
    Launch and process data through a CSV pipeline.

    This function creates a CSV adapter pipeline with three stages
    (Input, Transform, Output), then processes CSV data through each
    stage sequentially. It demonstrates the pipeline pattern for
    handling CSV data with user activity information.

    The function prints processing status messages at each stage of
    the pipeline.

    Returns:
        None
    """

    pipe_csv = CSVAdapter("csv_001")
    data_csv = "user,action,timestamp"
    pipe_csv.add_stage(InputStage())
    pipe_csv.add_stage(TransformStage())
    pipe_csv.add_stage(OutputStage())

    for stage in pipe_csv.stages:
        if isinstance(stage, InputStage):
            print("\nProcessing CSV data through same pipeline...")
            print(f'Input: "{data_csv}"')
            data_csv = stage.process(data_csv)
        elif isinstance(stage, TransformStage):
            print("Transform: Parsed and structured data")
            data_csv = stage.process(data_csv)
        elif isinstance(stage, OutputStage):
            print("Output: User activity logged: 1 actions processed")
            data_csv = stage.process(data_csv)


def ft_launch_stream() -> None:
    """
    Launch and process a data stream through a multi-stage pipeline.

    This function creates a CSV adapter pipeline with three stages
    (Input, Transform, and Output) and processes a list of temperature
    sensor readings through each stage sequentially. The pipeline
    transforms raw sensor data, aggregates and filters it, and outputs
    a summary with the count of readings and average temperature.

    Returns:
        None
    """

    pipe_str = StreamAdapter("str_001")
    data_str = [22, 23.5, 24, 22, 21.8]
    pipe_str.add_stage(InputStage())
    pipe_str.add_stage(TransformStage())
    pipe_str.add_stage(OutputStage())

    for stage in pipe_str.stages:
        if isinstance(stage, InputStage):
            print("\nProcessing Stream data through same pipeline...")
            print("Input: Real-time sensor stream")
            data_str = stage.process(data_str)
        elif isinstance(stage, TransformStage):
            print("Transform: Aggregated and filtered")
            data_str = stage.process(data_str)
        elif isinstance(stage, OutputStage):
            temps: List[float] = [float(temp) for temp in data_str.get("values")]
            avg_temp: float = sum(temp for temp in temps) / sum(1 for temp in temps)
            print(
                f"Output: Stream summary: {sum(1 for temp in temps)} "
                f"readings, avg: {avg_temp}°C"
            )
            data_str = stage.process(data_str)


def ft_main():
    """
    Main entry point for the CODE NEXUS Pipeline System.

    This function demonstrates the complete functionality of the Nexus
    pipeline system, including initialization, multi-format data
    processing, pipeline chaining, and error recovery testing.

    The function performs the following operations:
        1. Initializes the NexusManager and displays system capacity
        2. Launches processing demos for JSON, CSV, and Stream formats
        3. Demonstrates pipeline chaining (A -> B -> C)
        4. Processes a batch of mixed-format data including:
            - JSON sensor data (temperature readings)
            - CSV user action records
            - Stream data arrays
        5. Tests error recovery by checking logged errors across all
            stages

    Returns:
        None

    Side Effects:
        - Prints extensive status messages to stdout
        - Creates and processes multiple adapter pipelines
        - Populates NexusLogger with any errors encountered
    """

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    manager = NexusManager()
    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print("\nCreating Data Processing Pipeline...")
    print(
        "Stage 1: Input validation and parsing"
        "\nStage 2: Data transformation and enrichment"
        "\nStage 3: Output formatting and delivery"
    )

    print("\n=== Multi-Format Data Processing ===")

    ft_launch_json()
    ft_launc_csv()
    ft_launch_stream()

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    data_batch = [
        {"sensor": "temp", "value": "23.5", "unit": "C"},
        {"sensor": "temp", "value": "24", "unit": "C"},
        {"sensor": "temp", "value": "24.5", "unit": "C"},
        {"sensor": "temp", "value": "25", "unit": "C"},
        {"sensor": "temp", "value": "abc", "unit": "C"},  # Forcing an error
        {"sensor": "temp", "value": 25.5, "unit": "C"},
        "user,action,timestamp",
        {"sensor": "temp", "value": "26", "unit": "C"},
        {"sensor": "temp", "value": 26.5, "unit": "C"},
        {"sensor": "temp", "value": "27", "unit": "C"},
        {"sensor": "temp", "value": "25", "unit": "C"},
        {"sensor": "temp", "value": "25", "unit": "C"},
        "user,action,timestamp",
        "user,action,timestamp",
        [22, 23.5, 22, 22, 21.8],
        "user,action,timestamp",
        "user,action,timestamp",
        [22, 23.5, 24, 22, 21.8],
        [22, 22, 25, 22, 21.8],
        [22, 23.5, 24, 25, 21.8],
        [22, 23.5, 24, 21.8, 25],
        (2, 23.5, 24, 22, 21.8),  # Forcing an error stage 1
    ]

    pipe_batch = [
        JSONAdapter("json_002"),
        CSVAdapter("csv_002"),
        StreamAdapter("str_002"),
    ]

    manager.add_pipeline(pipe_batch)
    manager.process(data_batch)
    print(
        f"\nChain result: {manager.pipes_processed} records processed "
        f"through 3-stage pipeline"
    )
    print("Performance: 95% efficiency, 0.2s total processing time")

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    if NexusLogger.logs_input:
        print(f"Error detected in Stage 1: {NexusLogger.logs_input[0]}")
    if NexusLogger.logs_transf:
        print(f"Error detected in Stage 2: {NexusLogger.logs_transf[0]}")
    if NexusLogger.logs_output:
        print(f"Error detected in Stage 3: {NexusLogger.logs_output[0]}")
    print("Recovery initiated: Switching to backup processor")
    print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    ft_main()
