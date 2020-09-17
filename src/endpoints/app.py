import google.cloud.logging
from dotenv import load_dotenv
from fastapi import FastAPI

from . import type_games_endpoint

load_dotenv()

client = google.cloud.logging.Client()
client.setup_logging()


def create_app():
    app = FastAPI()
    app.include_router(type_games_endpoint.router)
    return app
