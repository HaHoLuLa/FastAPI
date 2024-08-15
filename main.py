from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import *
from database import get_db

app = FastAPI()

@app.get("/")
def read_root():
  return { "Hello": "World" }

@app.get("/member/{id}")
def read_member(id: str, db: Session = Depends(get_db)):
  db_item = get_member(db, id=id)
  if db_item is None:
    raise HTTPException(status_code=404, detail="items not found")
  return db_item
  
@app.get("/members")
def read_all(db: Session = Depends(get_db)):
  db_item = get_members(db)
  if db_item is None:
    raise HTTPException(status_code=404, detail="items not found")
  return db_item