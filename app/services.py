import httpx
import pandas as pd
from sqlalchemy.orm import Session
from . import models

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

async def get_pokemon_from_api(pokemon_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_URL}{pokemon_name.lower()}")

        if response.status_code != 200:
            return None
        
        data = response.json()

         #mapeo del json

        pokemon_data = {
            "id": data["id"], 
            "name": data["name"],
            "type_1": data["types"][0]["type"]["name"],
            "type_2": data["types"][0]["type"]["name"] if len(data["types"]) > 1 else None,
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "special_attack": data["stats"][3]["base_stat"],
            "special_defense": data["stats"][4]["base_stat"],
            "speed": data["stats"][5]["base_stat"],

            "sprite_url": data["sprites"]["front_default"]
        }
        return pokemon_data
    

async def get_pokemon_list(limit: int= 151):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_URL}?limit={limit}")
        return response.json()["results"]
    

def get_pokemon_stats_analysis(db:Session):

    query = db.query(models.Pokemon).all()
    
    data = [
        {
            "name": p.name,
            "type_1": p.type_1,
            "hp": p.hp,
            "attack": p.attack,
            "defense": p.defense
        } for p in query
    ]

    df = pd.DataFrame(data)

    analysis = df.groupby("type_1")["attack"].mean().sort_values(ascending=False)

    return analysis.to_dict()