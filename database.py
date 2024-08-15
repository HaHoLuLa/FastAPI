from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "mysql+pymysql://root:mariadb@localhost/bc2652"

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  except:
    db.close()
  finally:
    db.close()