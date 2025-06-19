import pytest
from fastapi.testclient import TestClient

from src.learning_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
