from unittest.mock import Mock

from src.bp import GetTypeGamesByUser
from src.bp import ParamsGetTypeGamesByUser


class ShouldGetTypeGamesByUserSteps:
    def given(self, user_id, types_games_mock):
        self.user_id = user_id
        self.types_games_mock = types_games_mock
        self.get_type_games_repository = Mock()
        self.get_type_games_repository.get_type_games_by_user = Mock(
            return_value=types_games_mock
        )
        self.get_all_type_games_use_case = GetTypeGamesByUser(
            self.get_type_games_repository
        )

    def when(self):
        self.response = self.get_all_type_games_use_case.run(
            ParamsGetTypeGamesByUser(self.user_id)
        )

    def then(self):
        assert self.response is not None
        assert len(self.response) == len(self.types_games_mock)
        self.get_type_games_repository.get_type_games_by_user.assert_called_with(
            self.user_id
        )
        self.get_type_games_repository.get_all_type_games.assert_not_called()
