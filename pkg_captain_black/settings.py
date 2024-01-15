"""Global configuration file for the project, to be subclassed for the sub projects.

Background
----------

This is the background to the approach taken here.

Objective
---------

The objective is to have a single source of truth for the settings that are shared between 
Platform apps.

Options
-------

Use .env files
^^^^^^^^^^^^^^



"""
import inspect
import json
import os


def this_directory() -> str:
    """Inspect the stack to find out where I have been called from."""
    # This approach is used to avoid relying on the location of the file, which is different for the children.
    # The calling frame is the second frame in the stack.
    calling_frame = inspect.stack()[1]
    calling_file_path = calling_frame.filename
    return os.path.dirname(calling_file_path)


class CaptainBlackSettings:
    """Settings that are shared between the packages.

    The settings can be overridden by providing a `settings.json` file in the same
    directory as the default settings.
    """

    app_name: str = "Captain Black Default Name"
    path: str = this_directory()
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_db: int = 1
    redis_address: str = f"redis://{redis_host}:{redis_port}/{redis_db}"
    log_format: str = "[%(asctime)s] [%(levelname)s] %(message)s. %(pathname)s:%(lineno)d, in %(funcName)s()"
    log_level: str = "WARN"  # as a string so it can be read and set in the settings.json.


    def __init__(self) -> None:
        """Load the dynamic settings then the alternative settings from the settings file."""
        # Custom settings
        self.load_local_settings(this_directory())

    # region Custom settings
    def load_local_settings(self, settings_directory: str) -> None:
        """Load custom settings from the local settings.json file."""
        settings_string = self._get_settings_file(settings_directory)
        settings = json.loads(settings_string)
        for key, value in settings.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def _get_settings_file(self, settings_directory: str) -> str:
        """Get the settings file as a json string."""
        settings_file = os.path.join(settings_directory, "settings.json")
        if os.path.isfile(settings_file):
            with open(settings_file, "r") as file:
                content = file.read()
            return content
        else:
            return "{}"

    # endregion


CAPTAIN_BLACK = CaptainBlackSettings()
