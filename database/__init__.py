from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database.models import *
"""
USAGE EXAMPLE:


from database import open_db
from database import User, Transaction

# open db and get handle functions
scope, clear = open_db('local_or_global_path_to_my_db')

# let create an user
user1 = User(public_key='438fxyfx4g9n2zdfdn258f2', ...)

# open session
with scope() as session:
    session.add(user1)

# You don't need to commit changes in db, session manager in case of success manage it
"""


def open_db(db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    Session = sessionmaker(bind=engine)

    @contextmanager
    def session_scope():
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def clear():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    Base.metadata.create_all(engine)

    return session_scope, clear
