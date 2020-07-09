from dataclasses import dataclass
from .usecase import UseCase


class GetAllTypeGamesUseCase(UseCase):

    def __init__(self, type_games_repository):
        self.type_games_repository = type_games_repository

    def run(self, params):
        type_games = self.type_games_repository.get_all_type_games(
            params.user_id)
        type_games.sort(key=lambda tg: tg.level, reverse=True)
        return type_games


@dataclass
class Params:
    user_id: str
 