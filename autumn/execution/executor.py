from typing import Protocol
from autumn.execution.task import Task


class Executor(Protocol):
    def execute(self, task: Task):
        ...


class PlainExecutor(Executor):
    def execute(self, task: Task):
        task.function.execute(task.input, task.output)
