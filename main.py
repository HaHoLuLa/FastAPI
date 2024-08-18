from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from crud import *
from database import get_db
from schemas import Member
from typing import List, Union

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # 모든 도메인에서의 접근을 허용합니다.
  allow_credentials=True,
  allow_methods=["*"],  # 모든 HTTP 메서드를 허용합니다.
  allow_headers=["*"],  # 모든 헤더를 허용합니다.
)

@app.get("/")
def read_root():
  return { "Hello": "World" }

@app.get("/member/{id}", response_model=Member)
def read_member(id: str, db: Session = Depends(get_db)):
  db_item = get_member(db, id=id)
  # if db_item is None:
  #   raise HTTPException(status_code=404, detail="items not found")
  return db_item
  
@app.get("/members", response_model=list[Member]) # , response_model=List[Member]
def read_all(db: Session = Depends(get_db)):
  db_item = get_members(db)
  # if len(db_item) <= 0:
  #   raise HTTPException(status_code=404, detail="items not found")
  return db_item


@app.post("/add", response_model=Member)
def member(member: Member, db: Session = Depends(get_db)):
  db_item = create_member(db, member=member)
  if db_item is None:
    raise HTTPException(status_code=404, detail="items not found")
  return db_item

@app.put("/member")
def update(member: Member, db: Session = Depends(get_db)):
  return None

@app.delete("/member")
def delete(member: Member, db: Session = Depends(get_db)):
  return None