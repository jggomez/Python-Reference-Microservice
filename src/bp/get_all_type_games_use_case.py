from dataclasses import dataclass

from data import GetAllTypeGamesRepository

from .usecase import UseCase


@dataclass
class Params:
    user_id: str


class GetAllTypeGamesUseCase(UseCase):
    def __init__(self, type_games_repository: GetAllTypeGamesRepository):
        self.type_games_repository = type_games_repository

    def run(self, params):
        type_games = self.type_games_repository.get_all_type_games(params.user_id)
        type_games.sort(key=lambda tg: tg.level, reverse=True)
        return type_games
