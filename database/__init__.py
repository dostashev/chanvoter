from contextlib import contextmanager
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from database.models import * 

def get_db_console(db_path):
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
