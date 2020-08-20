import logging

from bp import ParamsGetAllTypeGames
from bp import ParamsGetTypeGamesByUser
from di import providers
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from typing_extensions import Final

CODE: Final = "code"
MESSAGE: Final = "message"
ITEMS: Final = "items"
PAGE: Final = "page"

router = APIRouter()


@router.get("/apis/typegames/1.0.0")
def get_type_games(
    userid: str,
    codegame: str,
    page: int,
    maxitems: int,
    response: Response,
    get_all_type_game_uc=Depends(providers.all_type_games_use_case_module),
):
    try:
        logging.info(userid)
        resp = get_all_type_game_uc.run(ParamsGetAllTypeGames(userid))
        response_list = list([item.to_json() for item in resp])
        return {ITEMS: response_list, PAGE: page}
    except Exception as e:
        logging.error("Error in getalltypegames", exc_info=True)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {CODE: 500, MESSAGE: str(e)}


@router.get("/apis/typegamesbyuser/1.0.0")
def get_type_games_by_user(
    userid: str,
    page: int,
    maxitems: int,
    response: Response,
    get_type_game_by_user_uc=Depends(providers.type_games_by_user_use_case_module),
):
    try:
        logging.info(userid)
        resp = get_type_game_by_user_uc.run(ParamsGetTypeGamesByUser(userid))
        response_list = list([item.to_json() for item in resp])
        return {ITEMS: response_list, PAGE: page}
    except Exception as e:
        logging.error("Fatal error in gettypegamesbyuser", exc_info=True)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {CODE: 500, MESSAGE: str(e)}
