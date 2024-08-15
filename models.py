from sqlalchemy import Column, String
from database import Base

class Member(Base):
  __tablename__ = "member"

  id = Column(String, primary_key=True, index=True)
  pw = Column(String, index=True)
  name = Column(String, index=True)
  color = Column(String, index=True)
  