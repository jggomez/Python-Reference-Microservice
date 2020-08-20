import os

from typing_extensions import Final

URI_KEY: Final = "NEO4J_URI"
USER_KEY: Final = "NEO4J_USER"
PASSWORD_KEY: Final = "NEO4J_PASS"


class Config:
    URI_KEY = os.environ.get(URI_KEY)
    USER_KEY = os.environ.get(USER_KEY)
    PASSWORD_KEY = os.environ.get(PASSWORD_KEY)
