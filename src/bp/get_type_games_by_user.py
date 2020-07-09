from dataclasses import dataclass
from .usecase import UseCase


class GetTypeGamesByUser(UseCase):

    def __init__(self, type_games_repository):
        self.type_games_repository = type_games_repository

    def run(self, params):
        return self.type_games_repository.get_type_games_by_user(params.user_id)


@dataclass
class Params:
    user_id: str
