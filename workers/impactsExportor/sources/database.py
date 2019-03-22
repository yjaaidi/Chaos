from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def init_db(database_uri):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    engine = create_engine(database_uri)
    Base.session = scoped_session(sessionmaker(autocommit=False,
                                autoflush=False,
                                bind=engine))
    Base.query = Base.session.query_property()
