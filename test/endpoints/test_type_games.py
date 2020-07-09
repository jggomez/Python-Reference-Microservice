import pytest
from .steps.get_all_type_games_endpoint_steps import ShouldGetAllTypeGameSteps
from .steps.get_type_games_by_user_endpoint_steps import ShouldGetTypeGameByUserSteps


USER_ID_DATA_TEST = "USER_TEST_TYPE_GAMES"
TYPE_GAMES_ALL_DATA_TEST = [
    {
        "name": "type_game_1",
        "code": "PSICO",
        "hasmedals": False,
        "type": "ARCADE1",
        "url_background": "image1.png",
        "points": 20
    },
    {
        "name": "type_game_2",
        "code": "ING",
        "hasmedals": True,
        "type": "ARCADE2",
        "url_background": "image2.png",
        "points": 30
    },
    {
        "name": "type_game_3",
        "code": "ARQ",
        "hasmedals": False,
        "type": "ARCADE3",
        "url_background": "image3.png",
        "points": 10
    },
    {
        "name": "type_game_1",
        "code": "PSICO",
        "hasmedals": False,
        "type": "ARCADE1",
        "url_background": "image1.png",
        "points": 50
    }
]

TYPE_GAMES_BY_USER_DATA_TEST = [
    {
        "name": "type_game_1",
        "code": "PSICO",
        "hasmedals": False,
        "type": "ARCADE1",
        "url_background": "image1.png",
        "points": 20
    },
    {
        "name": "type_game_2",
        "code": "ING",
        "hasmedals": True,
        "type": "ARCADE2",
        "url_background": "image2.png",
        "points": 30
    },
    {
        "name": "type_game_3",
        "code": "ARQ",
        "hasmedals": False,
        "type": "ARCADE3",
        "url_background": "image3.png",
        "points": 10
    }
]


@pytest.mark.parametrize(
    "user_id, type_games",

    [(USER_ID_DATA_TEST, TYPE_GAMES_ALL_DATA_TEST)]

)
def test_should_get_all_type_games_endpoint(flask_test_client, user_id, type_games):
    test = ShouldGetAllTypeGameSteps()
    try:
        test.given(flask_test_client, user_id, type_games)
        test.when()
        test.then()
    finally:
        test.teardown()


@pytest.mark.parametrize(
    "user_id, type_games",

    [(USER_ID_DATA_TEST, TYPE_GAMES_BY_USER_DATA_TEST)]

)
def test_should_get_type_games_by_user_endpoint(flask_test_client, user_id, type_games):
    test = ShouldGetTypeGameByUserSteps()
    try:
        test.given(flask_test_client, user_id, type_games)
        test.when()
        test.then()
    finally:
        test.teardown()
