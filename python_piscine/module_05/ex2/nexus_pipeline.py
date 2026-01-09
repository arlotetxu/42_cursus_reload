from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import collections as col


class ProcessingStage(Protocol):

    def process(self, data) -> Any:
        ...


class InputStage:

    def process(self, data) -> Dict:
        ...


class TransformStage:

    def process(self, data) -> Dict:
        ...


class OutputStage:
    def process(self, data) -> Dict:
        ...

# ===========================================================================

class ProcessingPipeline(ABC):

    def __init__(self, pipe_id: str) -> None:
        self.pipe_id = pipe_id
        self.stages:List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data) -> Any:
        ...


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipe_id: str):
        super().__init__(pipe_id=pipe_id)

    def process(self, data):
        ...


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipe_id: str):
        super().__init__(pipe_id=pipe_id)

    def process(self, data):
        ...


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipe_id: str):
        super().__init__(pipe_id=pipe_id)

    def process(self, data):
        ...


# ==========================================================================
class NexusManager:

    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def process_data():
        ...
