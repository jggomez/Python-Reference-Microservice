import google.cloud.logging
from fastapi import FastAPI

from . import type_games_endpoint

client = google.cloud.logging.Client()
client.setup_logging()


def create_app():
    app = FastAPI()
    app.include_router(type_games_endpoint.router)
    return app
