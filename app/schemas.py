from pydantic import BaseModel
from typing import Optional

class PokemonBase(BaseModel):
    id: int
    name: str
    type_1: str
    type_2: Optional[str] = None
    hp: int
    attack: int
    defense: int
    sprite_url: str

class Pokemon(PokemonBase):
    class Config:
        from_attributes = True