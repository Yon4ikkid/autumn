from pydantic import BaseModel
from autumn.data.flow import Input, Output
from autumn.execution.function import Function


class Task(BaseModel):
    input: Input
    function: Function
    output: Output
