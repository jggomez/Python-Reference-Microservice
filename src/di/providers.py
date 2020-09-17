import os

from bp import GetAllTypeGamesUseCase
from bp import GetTypeGamesByUser
from data import GetAllTypeGamesRepository
from fastapi import Depends
from neo4j import DirectDriver
from neo4j import GraphDatabase
from typing_extensions import Final

URI_KEY: Final = "NEO4J_URI"
USER_KEY: Final = "NEO4J_USER"
PASSWORD_KEY: Final = "NEO4J_PASS"


def neo4j_driver_module() -> DirectDriver:
    uri_db = os.environ.get(URI_KEY)
    user_db = os.environ.get(USER_KEY)
    password_db = os.environ.get(PASSWORD_KEY)
    return GraphDatabase.driver(uri_db, auth=(user_db, password_db))


def type_games_repository_module(
    driver: DirectDriver = Depends(neo4j_driver_module),
) -> GetAllTypeGamesRepository:
    return GetAllTypeGamesRepository(driver)


def all_type_games_use_case_module(
    type_games_repository: GetAllTypeGamesRepository = Depends(
        type_games_repository_module
    ),
) -> GetAllTypeGamesUseCase:
    return GetAllTypeGamesUseCase(type_games_repository)


def type_games_by_user_use_case_module(
    type_games_repository: GetAllTypeGamesRepository = Depends(
        type_games_repository_module
    ),
) -> GetTypeGamesByUser:
    return GetTypeGamesByUser(type_games_repository)
