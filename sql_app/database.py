from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://pofzbtuanlyhum:c016fe76d833bc5c1eeb66bb0c8e070105308cffce5b384101162e2e777bddf4@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/d1eg01q97ttbua"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
