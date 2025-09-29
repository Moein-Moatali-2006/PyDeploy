from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/heroes/", response_model=dict)
def create_hero(name: str, secret_name: str, age: int | None = None, db: Session = Depends(get_db)):
    hero = models.Hero(name=name, secret_name=secret_name, age=age)
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return {"id": hero.id, "name": hero.name, "age": hero.age, "secret_name": hero.secret_name}


@app.get("/heroes/", response_model=list[dict])
def read_heroes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    heroes = db.query(models.Hero).offset(skip).limit(limit).all()
    return [{"id": h.id, "name": h.name, "age": h.age, "secret_name": h.secret_name} for h in heroes]

@app.get("/heroes/{hero_id}", response_model=dict)
def read_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.query(models.Hero).filter(models.Hero.id == hero_id).first()
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"id": hero.id, "name": hero.name, "age": hero.age, "secret_name": hero.secret_name}


@app.delete("/heroes/{hero_id}", response_model=dict)
def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.query(models.Hero).filter(models.Hero.id == hero_id).first()
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(hero)
    db.commit()
    return {"ok": True}


