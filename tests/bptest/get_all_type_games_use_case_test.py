import pytest

from .steps.get_all_type_games_use_case_steps import ShouldGetAllTypeGameSteps
from src.bp.domain import TypeGame

TYPE_GAMES__RETURN_DATA = [
    TypeGame(1, "game1", "image1", "ARCADE", "PSICO", "20", "Puntos", 0),
    TypeGame(2, "game2", "image2", "ARCADE", "ING", "10", "Puntos", 0),
    TypeGame(3, "game3", "image3", "ARCADE", "MED", "50", "Puntos", 0),
]

USER_ID_DATA = "test_user_get_type_games"


@pytest.mark.parametrize(
    "user_id, type_games", [(USER_ID_DATA, TYPE_GAMES__RETURN_DATA)]
)
def test_should_get_all_type_question(user_id, type_games):
    steps = ShouldGetAllTypeGameSteps()
    steps.given(user_id, type_games)
    steps.when()
    steps.then()
