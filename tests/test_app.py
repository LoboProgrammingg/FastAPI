from http import HTTPStatus

from fastapi.testclient import TestClient

from src.learning_fastapi.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organizacao do teste)

    response = client.get('/')  # Act (Acao do teste)

    assert (
        response.status_code == HTTPStatus.OK,
        response.json() == {'message': 'Hello, World'},
    )  # Assert (Verificacao do teste)
