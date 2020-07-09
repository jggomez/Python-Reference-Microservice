from ..util.util_neo4j import UtilNeo4j

CODE = "code"
NAME = "name"
LEVEL = "level"
TYPE_GAME_1_EXPECT = "type_game_1"
LEVEL_EXPECT = 50


class ShouldGetAllTypeGameSteps:

    def given(self, client, user_id, type_games):
        self.user_id = user_id
        self.client = client
        self.type_games = type_games
        self.util_neo4j = UtilNeo4j()
        self.util_neo4j.create_user(user_id, user_id)
        self.util_neo4j.create_type_games(self.type_games)
        self.util_neo4j.create_relationship_played_user_typegame(
            user_id, type_games)

    def when(self):
        self.response = self.client.get(
            f'/apis/typegames/1.0.0?userid={self.user_id}')

    def then(self):
        assert self.response is not None
        type_games = self.response.get_json()
        assert CODE not in type_games

        count_type_game = 0
        for tp in type_games:
            if tp[NAME] == TYPE_GAME_1_EXPECT:
                assert int(tp[LEVEL]) == LEVEL_EXPECT
                count_type_game = count_type_game + 1

        assert count_type_game == 1
        assert len(type_games) > 0

    def teardown(self):
        self.util_neo4j.delete_type_games_played_data_test(self.user_id)
