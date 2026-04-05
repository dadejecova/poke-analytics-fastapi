from sqlalchemy import Column, Integer, String
from .database import Base


class Pokemon(Base):
    __tablename__ = "Pokemons"

    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, unique=True, index=True)
    type_1 = Column(String)
    type_2 = Column(String, nullable=True)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sprite_url = Column(String)