from flask import request, Blueprint
from flask_expects_json import expects_json
from flask_api import status
from bp import GetAllTypeGamesUseCase
from bp import GetTypeGamesByUser
from bp import ParamsGetTypeGamesByUser
from bp import ParamsGetAllTypeGames
import logging

USER_ID = "userid"
CODE = "code"
MESSAGE = "message"

type_games_section = Blueprint('type_games_section', __name__)


@type_games_section.route('/apis/typegames/1.0.0', methods=['GET'])
def get_type_games(
        get_all_type_game_uc: GetAllTypeGamesUseCase):
    try:
        user_id = request.args.get(USER_ID)
        logging.info(user_id)
        resp = get_all_type_game_uc.run(
            ParamsGetAllTypeGames(user_id)
        )
        response_list = list([item.to_json() for item in resp])
        return response_list, status.HTTP_200_OK
    except Exception as e:
        logging.error("Error in getalltypegames",
                      exc_info=True)
        return {
            CODE: 500,
            MESSAGE: str(e)
        }, status.HTTP_500_INTERNAL_SERVER_ERROR


@type_games_section.route('/apis/typegamesbyuser/1.0.0', methods=['GET'])
def get_type_games_by_user(
        get_type_game_by_user_uc: GetTypeGamesByUser):
    try:
        user_id = request.args.get(USER_ID)
        logging.info(user_id)
        resp = get_type_game_by_user_uc.run(
            ParamsGetTypeGamesByUser(user_id)
        )
        response_list = list([item.to_json() for item in resp])
        return response_list, status.HTTP_200_OK
    except Exception as e:
        logging.error("Fatal error in gettypegamesbyuser",
                      exc_info=True)
        return {
            CODE: 500,
            MESSAGE: str(e)
        }, status.HTTP_500_INTERNAL_SERVER_ERROR
