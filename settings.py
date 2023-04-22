"""Configuration file for the project."""
from __future__ import annotations

import inspect
import os


def this_directory() -> str:
    """Inspect the stack to find out where I have been called from."""
    # This approach is used to avoid relying on the location of the file.
    # The calling frame is the second frame in the stack.
    calling_frame = inspect.stack()[1]
    calling_file_path = calling_frame.filename
    return os.path.dirname(calling_file_path)


class CaptainBlackSettings:
    """Class for keeping track of settings.  It doesn't need to be a dataclass because it is not being
    initialized from a dictionary or the pyproject.toml file.  It is just a class to hold the settings"""

    name: str = "Captain Black Default Name"
    path: str = this_directory()
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_db: int = 1
    redis_address: str = f"redis://{redis_host}:{redis_port}/{redis_db}"


CAPTAIN_BLACK = CaptainBlackSettings()