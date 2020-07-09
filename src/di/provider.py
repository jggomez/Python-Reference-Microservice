import os
import flask
import flask_injector
import injector
from neo4j import DirectDriver
from neo4j import GraphDatabase
from data import GetAllTypeGamesRepository
from bp import GetAllTypeGamesUseCase
from bp import GetTypeGamesByUser

URI_KEY = "URI_KEY"
USER_KEY = "USER_KEY"
PASSWORD_KEY = "PASSWORD_KEY"


class Neo4JDriverModule(injector.Module):
    def configure(self, binder):
        binder.bind(DirectDriver,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self, config: flask.Config) -> DirectDriver:
        uri_db = config.get(URI_KEY)
        user_db = config.get(USER_KEY)
        password_db = config.get(PASSWORD_KEY)
        return GraphDatabase.driver(uri_db, auth=(user_db, password_db))


class GetAllTypeGamesRepositoryModule(injector.Module):
    @injector.singleton
    def configure(self, binder):
        binder.bind(GetAllTypeGamesRepository,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self, driver: DirectDriver) -> GetAllTypeGamesRepository:
        return GetAllTypeGamesRepository(driver)


class GetAllTypeGamesUseCaseModule(injector.Module):
    def configure(self, binder):
        binder.bind(GetAllTypeGamesUseCase,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self, type_games_repository: GetAllTypeGamesRepository) -> GetAllTypeGamesUseCase:
        return GetAllTypeGamesUseCase(type_games_repository)


class GetTypeGamesByUserCaseModule(injector.Module):
    def configure(self, binder):
        binder.bind(GetTypeGamesByUser,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self, type_games_repository: GetAllTypeGamesRepository) -> GetTypeGamesByUser:
        return GetTypeGamesByUser(type_games_repository)
