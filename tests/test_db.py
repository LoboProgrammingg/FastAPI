from src.learning_fastapi.models import User


def test_create_user():
    user = User(
        username='matheusloboo',
        email='matheus@lobo.com',
        password='sarutobi12',
    )

    assert user.username == 'matheusloboo'