from pydantic import BaseModel

class Member(BaseModel):
  id: str
  pw: str
  name: str
  color: str
  class config:
    orm_mode = True