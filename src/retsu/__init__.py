"""Retsu."""

from importlib import metadata as importlib_metadata

from retsu.core import (
    ParallelTask,
    SerialTask,
    Task,
    TaskManager,
)
from retsu.tracking import (
    ResultTaskManager,
)


def get_version() -> str:
    """Return the program version."""
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "0.1.1"  # semantic-release


version = get_version()

__version__ = version
__author__ = "Ivan Ogasawara"
__email__ = "ivan.ogasawara@gmail.com"

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "ParallelTask",
    "ResultTaskManager",
    "SerialTask",
    "Task",
    "TaskManager",
]
