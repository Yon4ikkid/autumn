from typing import Protocol
from autumn.data.flow import Input, Output


class Function(Protocol):
    def execute(self, data_input: Input, data_output: Output):
        ...
