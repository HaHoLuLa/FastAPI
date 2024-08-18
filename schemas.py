from pydantic import BaseModel

class Member(BaseModel):
  id: str
  pw: str
  name: str
  color: str | None

# null 갑 포함이면 유니온 타입 정의