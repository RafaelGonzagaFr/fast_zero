from sqlalchemy import select, update

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


def test_update_at(session):
    user = User(
        username='gonzaga', email='rafael@gmail.com', password='olamundo'
    )

    session.add(user)
    session.commit()

    user = User(
        username='gonzaga', email='rafael@gmail.com', password='olamundo'
    )

    session.execute(
        update(User),
        [
            {
                'id': 1,
                'username': 'gonzaga',
                'email': 'rafael@gmail.com',
                'password': '123',
            }
        ],
    )

    result = session.scalar(
        select(User).where(User.email == 'rafael@gmail.com')
    )

    session.commit()

    print(User)

    assert result.username == 'gonzaga'
