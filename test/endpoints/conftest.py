import sys
import pytest
sys.path.append("../src/")
from src.endpoints import create_app
from src.endpoints.config import Config
from src.di import provider


@pytest.fixture
def app():
    app = create_app(
        config_object=Config
    )
    app.testing = True

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
