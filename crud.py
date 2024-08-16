from sqlalchemy.orm import Session
from models import Member
from schemas import Member as SMember

def get_member(db: Session, id: str):
  return db.query(Member).filter(Member.id == id).first()

def get_members(db: Session):
  return db.query(Member).all()

def create_member(db: Session, member: SMember):
  db_member = Member(
    id = member.id,
    pw = member.pw,
    name = member.name,
    color = member.color
  )
  db.add(db_member)
  db.commit()
  db.refresh(db_member)
  return db_member

def update_member(db: Session, member: SMember):
  db_member = db.query(Member).filter(Member.id == member.id).first()
  if db_member is None:
    return None
  if member.name:
    db_member.name = member.name
  if member.color:
    db_member.color = member.color
  db.commit()
  db.refresh(db_member)
  return db_member

def delete_member(db: Session, id: str):
  db_member = db.query(Member).filter(Member.id == id).first()
  if db_member is None:
    return None
  db.delete(db_member)
  db.commit()
  return db_member