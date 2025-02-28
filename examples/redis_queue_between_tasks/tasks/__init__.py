"""Tasks for the example."""

from retsu import TaskManager

from .parallel import MyParallelTask1
from .serial import MySerialTask1


class MyTaskManager(TaskManager):
    """MyTaskManager."""

    def __init__(self) -> None:
        """Create a list of retsu tasks."""
        self.tasks = {
            "serial": MySerialTask1(),
            "parallel": MyParallelTask1(workers=2),
        }
