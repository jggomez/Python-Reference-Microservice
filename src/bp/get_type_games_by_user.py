from dataclasses import dataclass

from data import GetAllTypeGamesRepository

from .usecase import UseCase


@dataclass
class Params:
    user_id: str


class GetTypeGamesByUser(UseCase):
    def __init__(self, type_games_repository: GetAllTypeGamesRepository):
        self.type_games_repository = type_games_repository

    def run(self, params):
        return self.type_games_repository.get_type_games_by_user(params.user_id)
