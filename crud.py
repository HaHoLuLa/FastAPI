from sqlalchemy.orm import Session
from models import Member

def get_member(db: Session, id: str):
  return db.query(Member).filter(Member.id == id).first()

def get_members(db: Session):
  return db.query(Member).all()

