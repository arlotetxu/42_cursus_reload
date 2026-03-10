from typing import List, Dict, Any, Self
from pydantic import BaseModel, Field, model_validator, ValidationError
from src.conf.enums import Colors
from icecream import ic

'''
The zones coordinates will always be positive integers, and there
will always be a unique start and a unique end zone.


'''

class DataValidator(BaseModel):

    map_connects: List[tuple[str, str]] = Field(...)

    @model_validator(mode='after')
    def check_connections(self) -> Self:
        for con in self.map_connects:
            if con[0] is con[1]:
                raise ValidationError(
                    f"{Colors.RED.value}[Error] - Same hubs in connection!"
                    f"{Colors.RESET.value}"
                )
        return self
