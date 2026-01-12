#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Protocol, Union, runtime_checkable

from icecream import ic


@runtime_checkable
class ProcessingStage(Protocol):
    def process(self, data) -> Any: ...


# No contructor parameters required
class InputStage:
    def process(self, data: Any) -> Dict:
        '''
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        '''
        input_ret: Dict = {}
        # ic("Estoy en InputStage")
        required_keys = ["sensor", "value", "unit"]
        if isinstance(data, dict) and all(key in data for key in required_keys):
            print("\nProcessing JSON data through pipeline...")
            print(f"Input: {data}")
            input_ret = {**data}
            input_ret['from'] = "json"
            # ic(input_ret)

        elif isinstance(data, str) and "," in data:
            print("\nProcessing CSV data through same pipeline...")
            print(f"Input: \"{data}\"")
            input_ret["string"] = data.split(",")
            input_ret["from"] = "csv"
            # ic(input_ret)

        elif isinstance(data, List) and all(isinstance(item, ((int, float))) for item in data):
            print("\nProcessing Stream data through same pipeline...")
            print("Input: Real-time sensor stream")
            input_ret["values"] = data
            input_ret["from"] = "stream"
            # ic(input_ret)
        else:
            print("\nERROR. Data input not recognized!!")

        # ic(input_ret)
        return input_ret



# No contructor parameters required
class TransformStage:
    '''
    ic| data: {'from': 'json', 'sensor': 'temp', 'unit': 'C', 'value': 23.5}
    ic| data: {'from': 'csv', 'string': ['Esto', 'es', 'un', 'string']}
    ic| data: {'from': 'stream', 'values': [22, 23.5, 24, 22, 21.8]}
    '''
    def process(self, data: Any) -> Dict:
        # ic("Estoy en TransformStage")
        for k, v in data.items():
            if k == "from" and v == "json":
                print("Transform: Enriched with metadata and validation")
            if k == "from" and v == "csv":
                print("Transform: Parsed and structured data")
            if k == "from" and v == "stream":
                print("Transform: Aggregated and filtered")
        data["processed"] = True
        return data


# No contructor parameters required
class OutputStage:
    '''
    ic| data: {'from': 'json', 'sensor': 'temp', 'unit': 'C', 'value': 23.5}
    ic| data: {'from': 'csv', 'string': ['Esto', 'es', 'un', 'string']}
    ic| data: {'from': 'stream', 'values': [22, 23.5, 24, 22, 21.8]}
    '''
    def process(self, data: Any) -> Dict:
        # ic("Estoy en Outputstage")
        for k, v in data.items():
            if k == "from" and v == "json":
                try:
                    temp: float = float(data.get("value"))
                    range: str = "Normal Range" if temp > 0 and temp < 100 else "Out of Range"
                    print(f"Output: Processed temperature reading: {temp:.1f}°C ({range})")
                except (KeyError, ValueError):
                    print("ERROR: temp value is not a number")
            if k == "from" and v == "csv":
                print("Output: User activity logged: 1 actions processed")
            if k == "from" and v == "stream":
                try:
                    temps: List[float] = [float(temp) for temp in data.get("values")]
                    avg_temp: float = sum(temp for temp in temps) / sum(1 for temp in temps)
                    print(f"Output: Stream summary: {sum(1 for temp in temps)} readings, avg: {avg_temp}°C")
                except (ValueError):
                    print("ERROR. Some of the temps are not a number")


# ===========================================================================


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]: ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        # ic("==================================")
        # ic("En process de JSONAdapter")
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        # ic("==================================")
        # ic("En process de CSVAdapter")
        for stage in self.stages:
            data = stage.process(data)
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        # ic("==================================")
        # ic("En process de StreamAdapter")
        for stage in self.stages:
            data = stage.process(data)
        return data


# ==========================================================================
class NexusManager:
    def __init__(self):
        self.pipelines: List[Any] = []  # TODO debe ser col.deque?
        self.capacity = 1000

    def add_pipeline(self, pipelines: List[ProcessingPipeline]):
        for pipeline in pipelines:
            self.pipelines.append(pipeline)

    def process(self, data: Any):
        # ic(self.pipelines)
        for pipe in self.pipelines:
            pipe.add_stage(InputStage())
            pipe.add_stage(TransformStage())
            pipe.add_stage(OutputStage())
            pipe.process(data)
        self.pipelines.clear()


        # ic(ProcessingPipeline.stages)


# ===========================================================================


def ft_main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    manager = NexusManager()
    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing"
          "\nStage 2: Data transformation and enrichment"
          "\nStage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===")


    pipe_json = JSONAdapter("json_001")
    data_json = {"sensor": "temp", "value": "23.5", "unit": "C"}
    manager.add_pipeline([pipe_json])
    manager.process(data_json)

    pipe_csv = CSVAdapter("csv_001")
    data_csv = "Esto,es,un,string"
    manager.add_pipeline([pipe_csv])
    manager.process(data_csv)

    pipe_stream = StreamAdapter("str_001")
    data_str = [22, 23.5, 24, 22, 21.8]
    manager.add_pipeline([pipe_stream])
    manager.process(data_str)

    pipe_error = StreamAdapter("err_001")
    data_error = {21, 22, 23}
    manager.add_pipeline([pipe_error])
    manager.process(data_error)

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")


if __name__ == "__main__":
    ft_main()
