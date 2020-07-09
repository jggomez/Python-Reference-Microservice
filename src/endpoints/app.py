import google.cloud.logging
from flask_api import FlaskAPI
import flask_injector
import injector
from di import provider
from .type_games_endpoint import type_games_section

client = google.cloud.logging.Client()
client.setup_logging()

INJECTOR_DEFAULT_MODULES = dict(
    driver=provider.Neo4JDriverModule(),
    get_all_type_games_repository=provider.GetAllTypeGamesRepositoryModule(),
    get_all_type_games_use_case=provider.GetAllTypeGamesUseCaseModule(),
    get_type_games_by_user_use_case=provider.GetTypeGamesByUserCaseModule()
)


def _configure_dependency_injection(flask_app, injector_modules,
                                    custom_injector):
    modules = dict(INJECTOR_DEFAULT_MODULES)
    if injector_modules:
        modules.update(injector_modules)

    flask_injector.FlaskInjector(
        app=flask_app,
        injector=custom_injector,
        modules=modules.values()
    )


def create_app(
    *,
    config_object,
    custom_injector: injector.Injector = None,
    injector_modules=None,
):
    app = FlaskAPI(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(type_games_section)
    _configure_dependency_injection(app, injector_modules, custom_injector)
    return app
