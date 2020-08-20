from dataclasses import dataclass

from typing_extensions import Final

# Constants
ID: Final = "id"
NAME: Final = "name"
URL_BACKGROUND: Final = "urlbackground"
CODE: Final = "code"
TYPE: Final = "type"
HAS_MEDALS: Final = "hasmedals"
LEVEL: Final = "level"
NAME_LEVEL: Final = "namelevel"
PROGRESSION: Final = "progression"


@dataclass(frozen=True)
class TypeGame:
    id: int
    name: str
    url_background: str
    code: str
    type: str
    level: str = ""
    namelevel: str = ""
    progression: int = 0

    def to_json(self):
        return {
            ID: self.id,
            NAME: self.name,
            URL_BACKGROUND: self.url_background,
            CODE: self.code,
            TYPE: self.type,
            LEVEL: self.level,
            NAME_LEVEL: self.namelevel,
            PROGRESSION: self.progression,
        }
