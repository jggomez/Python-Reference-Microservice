import os

from neo4j import GraphDatabase

# Constants
URI_KEY = "NEO4J_URI"
USER_KEY = "NEO4J_USER"
PASSWORD_KEY = "NEO4J_PASS"
NAME = "name"
CODE = "code"
HAS_MEDALS = "hasmedals"
TYPE = "type"
URL_BACKGROUND = "url_background"
POINTS = "points"

driver_neo4j = None

SENTENCE_CREATE_USER = """
CREATE (u:USER)
SET u.id = "{}"
SET u.name = "{}"
"""

SENTENCE_CREATE_TYPE_GAME = """
MERGE (typeGame:TYPEGAME{{name:'{}', code:'{}', hasMedals:'{}', type:'{}', urlbackground:'{}'}})
"""

SENTENCE_CREATE_RELATIONSHIP_TYPE_GAME_USER = """
MATCH (user:USER{{id:'{}'}})
MATCH (typeGame:TYPEGAME{{name:'{}'}})
MERGE (user) - [:IS_PLAYING] -> (typeGame)
"""

SENTENCE_CREATE_RELATIONSHIP_PLAYED_TYPE_GAME_USER = """
MATCH (user:USER{{id:'{}'}})
MATCH (typeGame:TYPEGAME{{name:'{}'}})
MERGE (user) - [:PLAYED{{points:{}}}] -> (typeGame)
"""

SENTENCE_DELETE_PLAYING_DATA_TEST = """
MATCH (user:USER)
WHERE user.id = "{}"
OPTIONAL MATCH (user) - [:IS_PLAYING] - (typeGame:TYPEGAME)
DETACH DELETE user, typeGame
"""

SENTENCE_DELETE_PLAYED_DATA_TEST = """
MATCH (user:USER)
WHERE user.id = "{}"
OPTIONAL MATCH (user) - [:PLAYED] - (typeGame:TYPEGAME)
DETACH DELETE user, typeGame
"""


class UtilNeo4j:
    def _create_driver_neo4j(self):
        uri = os.environ.get(URI_KEY)
        user = os.environ.get(USER_KEY)
        password = os.environ.get(PASSWORD_KEY)
        return GraphDatabase.driver(uri, auth=(user, password))

    def create_user(self, user_id, name):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            session.write_transaction(self._create_user_neo4j, user_id, name)

    @staticmethod
    def _create_user_neo4j(tx, user_id, name):
        tx.run(SENTENCE_CREATE_USER.format(user_id, name))

    def create_type_games(self, type_games):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            for type_game in type_games:
                session.write_transaction(self._create_type_game, type_game)

    @staticmethod
    def _create_type_game(tx, type_game):
        tx.run(
            SENTENCE_CREATE_TYPE_GAME.format(
                type_game[NAME],
                type_game[CODE],
                type_game[HAS_MEDALS],
                type_game[TYPE],
                type_game[URL_BACKGROUND],
            )
        )

    def create_relationship_user_typegame(self, user_id, type_games):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            for type_game in type_games:
                session.write_transaction(
                    self._create_relationship_user_typegame_neo4j,
                    user_id,
                    type_game[NAME],
                )

    @staticmethod
    def _create_relationship_user_typegame_neo4j(tx, user_id, type_game_name):
        tx.run(
            SENTENCE_CREATE_RELATIONSHIP_TYPE_GAME_USER.format(user_id, type_game_name)
        )

    def delete_type_games_played_data_test(self, user_id):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            session.write_transaction(
                self._delete_type_games_played_data_test_neo4j, user_id
            )

    @staticmethod
    def _delete_type_games_played_data_test_neo4j(tx, user_id):
        tx.run(SENTENCE_DELETE_PLAYED_DATA_TEST.format(user_id))

    def delete_type_games_playing_data_test(self, user_id):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            session.write_transaction(
                self._delete_type_games_playing_data_test_neo4j, user_id
            )

    @staticmethod
    def _delete_type_games_playing_data_test_neo4j(tx, type_game_name):
        tx.run(SENTENCE_DELETE_PLAYING_DATA_TEST.format(type_game_name))

    def create_relationship_played_user_typegame(self, user_id, type_games):
        driver_neo4j = self._create_driver_neo4j()
        with driver_neo4j.session() as session:
            for type_game in type_games:
                session.write_transaction(
                    self._create_relationship_played_user_typegame_neo4j,
                    user_id,
                    type_game[NAME],
                    type_game[POINTS],
                )

    @staticmethod
    def _create_relationship_played_user_typegame_neo4j(
        tx, user_id, type_game_name, points
    ):
        tx.run(
            SENTENCE_CREATE_RELATIONSHIP_PLAYED_TYPE_GAME_USER.format(
                user_id, type_game_name, points
            )
        )
