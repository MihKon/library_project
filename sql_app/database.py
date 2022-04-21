from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://nygcwesjxgzvwn:236d8084a782336107b50eefa017c78ba9c592b42dbac45baefce4ec4c84484f@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/del6ctkpuulplj"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
