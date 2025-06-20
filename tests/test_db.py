from sqlalchemy import select

from src.learning_fastapi.models import User


def test_create_user(session):
    user = User(
        username='test',
        email='test@lobo.com',
        password='sarutobi12',
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'test@lobo.com'))

    assert result.id == 1
