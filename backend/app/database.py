from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./pokemon.db"

# engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread":False}
)

# sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()