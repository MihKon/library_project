from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://qtamtnwlzwammm:7435683321aa9ccfd1524a01b8aeb2e85d9f8014ad2fbab47d7fb68fe7701d66@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d8dqp0t5thoh68"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
