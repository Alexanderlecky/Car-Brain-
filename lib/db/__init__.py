from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base

DATABASE_URL = 'sqlite:///app.db'

def init_db():
    # Create the engine and the database
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    
    # Create a configured "Session" class
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    return Session()
