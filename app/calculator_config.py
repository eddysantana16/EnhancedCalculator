import os
from app.exceptions import ConfigurationError

def load_config():
    history_file = os.getenv("HISTORY_FILE")
    if not history_file:
        raise ConfigurationError("HISTORY_FILE environment variable not set")
    return {"HISTORY_FILE": history_file}
