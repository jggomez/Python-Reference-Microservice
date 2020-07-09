from ..util.util_neo4j import UtilNeo4j

CODE = "code"


class ShouldGetTypeGameByUserSteps:

    def given(self, client, user_id, type_games):
        self.client = client
        self.user_id = user_id
        self.type_games = type_games
        self.util_neo4j = UtilNeo4j()
        self.util_neo4j.create_user(user_id, user_id)
        self.util_neo4j.create_type_games(type_games)
        self.util_neo4j.create_relationship_user_typegame(
            user_id, type_games)

    def when(self):
        self.response = self.client.get(
            f'/apis/typegamesbyuser/1.0.0?userid={self.user_id}')

    def then(self):
        assert self.response is not None
        type_games_resp = self.response.get_json()
        assert CODE not in type_games_resp
        assert len(type_games_resp) > 0
        assert len(type_games_resp) == len(self.type_games)

    def teardown(self):
        self.util_neo4j.delete_type_games_playing_data_test(self.user_id)
