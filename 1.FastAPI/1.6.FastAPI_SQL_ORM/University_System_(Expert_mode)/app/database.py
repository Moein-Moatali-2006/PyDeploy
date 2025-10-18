from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://moein_user:moein_pass@localhost:5432/university_db"
SQLALCHEMY_DATABASE_URL = "postgresql://root:y8w83I4IKoudOQgchcA4Lydv@moein-moatali:5432/postgres" #Liara

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()