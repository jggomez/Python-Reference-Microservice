from src.bp import GetAllTypeGamesUseCase
from unittest.mock import Mock
from src.bp import ParamsGetAllTypeGames


class ShouldGetAllTypeGameSteps:

    def given(self, user_id, types_games_mock):
        self.user_id = user_id
        self.types_games_mock = types_games_mock
        self.get_type_games_repository = Mock()
        self.get_type_games_repository.get_all_type_games = Mock(
            return_value=types_games_mock
        )
        self.get_all_type_games_use_case = GetAllTypeGamesUseCase(
            self.get_type_games_repository
        )

    def when(self):
        self.response = self.get_all_type_games_use_case.run(
            ParamsGetAllTypeGames(self.user_id)
        )

    def then(self):
        assert self.response is not None
        assert len(self.response) == len(self.types_games_mock)

        self.types_games_mock.sort(
            key=lambda type_game: type_game.level, reverse=True)
        for type_games, type_games_mock in zip(self.response, self.types_games_mock):
            assert type_games.id == type_games_mock.id
            assert type_games.name == type_games_mock.name
            assert type_games.level == type_games_mock.level

        self.get_type_games_repository.get_all_type_games.assert_called()
        self.get_type_games_repository.get_type_games_by_user.assert_not_called()
