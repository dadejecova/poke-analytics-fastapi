from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, services
from .database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PokeAnalytics API")

@app.get("/pokemon/{name}", response_model=schemas.Pokemon)
async def get_pokemon(name: str, db: Session = Depends(get_db)):
    name = name.lower()

    db_pokemon = db.query(models.Pokemon).filter(models.Pokemon.name == name).first()

    if db_pokemon:
        print("Se encontró en local")
        return db_pokemon
    
    # Si no esta en la db se busca en pokeapi
    print("No esta en la bd, buscamos en la API")
    api_data = await services.get_pokemon_from_api(name)

    if not api_data:
        raise HTTPException(status_code=404, detail = "Pokemon no encontrado")
    
    # Guardamos en la bd para una siguiente vez
    new_pokemon = models.Pokemon(**api_data)
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)

    return new_pokemon

@app.post("/sync-pokemon")
async def sync_pokemon(db: Session = Depends(get_db)):
    #nombres lista
    pokemon_list = await services.get_pokemon_list(151)

    counter = 0
    for item in pokemon_list:
        name = item["name"]

        #Verificacion por duplicaods
        exists = db.query(models.Pokemon).filter(models.Pokemon.name == name).first()

        if not exists:
            #si no existe reusamos el codigo
            pokemon_data = await services.get_pokemon_from_api(name)
            if pokemon_data:
                new_poke = models.Pokemon(**pokemon_data)
                db.add(new_poke)
                counter += 1

    db.commit()
    return {"message": f"Sincronización completada. {counter} Nuevos pokos agregados"}


@app.get("/pokemons", response_model=List[schemas.Pokemon])
def get_all_pokemons(db: Session = Depends(get_db)):
    # Consulta a la tabla
    pokemons = db.query(models.Pokemon).all()
    return pokemons


@app.get("/analytics/attack_by-type")
def get_attack_analysis(db: Session = Depends(get_db)):
    analysiss = services.get_pokemon_stats_analysis(db)
    return analysiss