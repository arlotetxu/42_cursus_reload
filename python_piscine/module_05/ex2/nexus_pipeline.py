#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol, runtime_checkable
import collections as col
from icecream import ic


@runtime_checkable
class ProcessingStage(Protocol):

    def process(self, data) -> Any:
        ...


# No contructor parameters required
class InputStage:

    def process(self, data:Any) -> Dict:
        ...


# No contructor parameters required
class TransformStage:

    def process(self, data:Any) -> Dict:
        ...


# No contructor parameters required
class OutputStage:
    def process(self, data:Any) -> Dict:
        ...

# ===========================================================================

class ProcessingPipeline(ABC):

    #def __init__(self) -> None:
        #self.pipeline_id = pipeline_id
    stages:List[ProcessingStage] = []

    def add_stage(stage: ProcessingStage) -> None:
        ProcessingPipeline.stages.append(stage)

    @abstractmethod
    def process(data:Any) -> Union[str, Any]:
        ...


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data:Any) -> Union[str, Any]:
        ...


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data:Any) -> Union[str, Any]:
        ...


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data:Any) -> Union[str, Any]:
        ...


# ==========================================================================
class NexusManager:

    def __init__(self):
        self.pipelines: List[Any] = [] # TODO debe ser col.deque?

    def add_pipeline(self, pipeline: Dict[str: Dict[Any]]):
        self.pipelines.append(pipeline)

    def process_data(self):
        input_s = InputStage()
        trans_s = TransformStage()
        output_s = OutputStage()

        if isinstance(input_s, ProcessingStage):
            ProcessingPipeline.add_stage(input_s)
        if isinstance(trans_s, ProcessingStage):
            ProcessingPipeline.add_stage(trans_s)
        if isinstance(output_s, ProcessingStage):
            ProcessingPipeline.add_stage(output_s)

        ic(ProcessingPipeline.stages)

# ===========================================================================

def ft_main():

    manager = NexusManager()

    json = {
            "JSON": {"type": "sensor", "temp": 22.5, "magn": 'F'}
            }
    csv = {
            "CSV": {"type": "log", "events": "user,action,timestamp"}
            }
    stream = {
            "stream": {"type": "stream", "temps": [22, 23, 24, 25, 26]}}
    
    manager.add_pipeline(json)
    manager.add_pipeline(csv)
    manager.add_pipeline(stream)

    ic(manager.pipelines)

    manager.process_data()

if __name__ == "__main__":
    ft_main()
