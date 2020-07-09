from dataclasses import dataclass

# Constants
ID = "id"
NAME = "name"
URL_BACKGROUND = "urlbackground"
CODE = "code"
TYPE = "type"
HAS_MEDALS = "hasmedals"
LEVEL = "level"
NAME_LEVEL = "namelevel"
PROGRESSION = "progression"


@dataclass(frozen=True)
class TypeGame():
    id: int
    name: str
    url_background: str
    code: str
    type: str
    level: str = ""
    namelevel: str = ""
    progression: int = 0

    def to_json(self):
        return {ID: self.id,
                NAME: self.name,
                URL_BACKGROUND: self.url_background,
                CODE: self.code,
                TYPE: self.type,
                LEVEL: self.level,
                NAME_LEVEL: self.namelevel,
                PROGRESSION: self.progression
                }
