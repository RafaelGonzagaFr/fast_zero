from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='gonzaga', email='rafael@gmail.com', password='olamundo'
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'rafael@gmail.com')
    )

    assert result.username == 'gonzaga'
