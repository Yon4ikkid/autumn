from autumn.data.flow import Input, Output
from autumn.data.repository import Repository
from autumn.execution.executor import Executor
from autumn.execution.function import Function
from autumn.execution.task import Task


class RunCommand(Function):
    def __init__(self, repository: Repository):
        self._command_repository = repository

    def execute(self, data_input: Input, data_output: Output):
        pass
