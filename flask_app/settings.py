"""Settings for the Flask app."""
from pkg_shared.settings import CaptainBlackSettings, this_directory


class FlaskAppSettings(CaptainBlackSettings):
    """Settings for pkg_config app."""

    _MINUTE: int = 60

    log_directory = "logs/flask_api_v1_v2"
    cache_lifetime: int = _MINUTE * 10

    def __init__(self) -> None:
        """Load the custom settings from the parent, then the local ones."""
        super().__init__()
        self.load_local_settings(this_directory())


FLASK_APP = FlaskAppSettings()
